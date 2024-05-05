import os
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
from langchain.agents import  Tool
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, ReadOnlySharedMemory
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun

llm = ChatGroq(temperature=0, groq_api_key="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", model_name="llama3-70b-8192")

template = """This is a conversation between a human and ai agent:

{chat_history}

Write a summary of the conversation for {input}:
"""

prompt = PromptTemplate(input_variables=["input", "chat_history"], template=template)
memory = ConversationBufferMemory(memory_key="chat_history")
readonlymemory = ReadOnlySharedMemory(memory=memory)
summary_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=readonlymemory,  # use the read-only memory to prevent the tool from modifying the memory
)

#create searches
search =  DuckDuckGoSearchRun()

tool_use = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
    ),
    Tool(
        name="Summary",
        func=summary_chain.run,
        description="useful for when you summarize a conversation. The input to this tool should be a string, representing who will read this summary.",
    )
    
]

tool_use_1 = [
    Tool(
        name="Summary",
        func=summary_chain.run,
        description="useful for when you summarize a conversation. The input to this tool should be a string, representing who will read this summary.",
    )
]

# Define Agents
email_author = Agent(
    role='Professional Email Author',
    goal='Craft concise and engaging emails',
    backstory='Experienced in writing impactful marketing emails.',
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=tool_use
)
marketing_strategist = Agent(
    role='Marketing Strategist',
    goal='Lead the team in creating effective cold emails',
    backstory='A seasoned Chief Marketing Officer with a keen eye for standout marketing content.',
    verbose=True,
    allow_delegation=True,
    llm=llm,
    tools=tool_use_1
)

content_specialist = Agent(
    role='Content Specialist',
    goal='Critique and refine email content',
    backstory='A professional copywriter with a wealth of experience in persuasive writing.',
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=tool_use_1
    )


# Define Task
email_task = Task(
    description='''1. Generate two distinct variations of a cold email promoting a video editing solution. 
    2. Evaluate the written emails for their effectiveness and engagement.
    3. Scrutinize the emails for grammatical correctness and clarity.
    4. Adjust the emails to align with best practices for cold outreach. Consider the feedback 
    provided to the marketing_strategist.
    5. Revise the emails based on all feedback, creating two final versions.''',
    agent=marketing_strategist  # The Marketing Strategist is in charge and can delegate
)

# Create a Single Crew
email_crew = Crew(
    agents=[email_author, marketing_strategist, content_specialist],
    tasks=[email_task],
    verbose=True,
    process=Process.sequential
)

# Execution Flow
print("Crew: Working on Email Task")
emails_output = email_crew.kickoff()
