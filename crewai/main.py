import os

os.environ["SERPER_API_KEY"] = "991f5608e25ea4cbb4c7b958e8b5c0adbd1bf262"  # serper.dev API key
os.environ["OPENAI_API_KEY"] = "sk-proj-S9aYVQCFpMb9gdZee0EVT3BlbkFJ2C1vFeXNXwtwmLmoB8d6"
db_uri="""postgresql://cpradmin:Apr1l2024@cprpostgres-db.postgres.database.azure.com:5432/cprcashier"""


from crewai import Agent
from crewai_tools import SerperDevTool
from crewai_tools import PGSearchTool
from crewai import Task

# Initialize the tool with the database URI and the target table name
#my_tool = PGSearchTool(db_uri=db_uri, table_name='transactions', verbose=True, memory=True, cache=True, max_rpm=100, share_crew=True, allow_delegation=True, backstory="You are a sql database expert with a passion for analyzing data")
transactions_tool = PGSearchTool(db_uri=db_uri, table_name='transactions')
products_tool = PGSearchTool(db_uri=db_uri, table_name='products')
customers_tool = PGSearchTool(db_uri=db_uri, table_name='customers')
planogram_tool = PGSearchTool(db_uri=db_uri, table_name='planogram')
stores_tool = PGSearchTool(db_uri=db_uri, table_name='stores')
recommendations_tool = PGSearchTool(db_uri=db_uri, table_name='recommendations')

search_tool = SerperDevTool() # To do a search on the internet

# Creating a senior analyst agent with memory and verbose mode
researcher = Agent(
    role='Senior Analyst',
    goal='Do the  {question}',
    verbose=True,
    memory=True,
    backstory=(
        "You are the main optimizer agent building an optimization plan based on information from your worker agents"
        "Your mission is to be create the text for a final report on how improvements can be made based on the data you receive"
    ),
    allow_delegation=True
)

# Creating a transactions agent with custom tools and delegation capability
data_analyst = Agent(
    role='Transactions',
    goal='Based on the {question} retrieve and analyse relevant data',
    verbose=True,
    memory=True,
    backstory=(
        "You are a sql database expert with a passion for analyzing data"
    ),

    tools=[transactions_tool, products_tool, customers_tool, planogram_tool, stores_tool, recommendations_tool],
    allow_delegation=True
)


# Research task
research_task = Task(
    description=(
        "Answer the following {question}."
        "Focus on data provided from the data_analyst {question}."
        "Use the web search tool to find the latest information on retail market trends based on what your store currently sells."
    ),
    expected_output='A comprehensive 4 paragraph answer to the question suggesting areas of improvement.',
    tools=[search_tool],
    agent=researcher
)

# Recommendations task with language model configuration
data_analysis_task = Task(
    description=(
        "Based on the initial {question}."
        "Make recommendations on improvement"
        "Search the web if you need up to date information on retail market trends based on what your store currently sells"
    ),
    expected_output='A 4 paragraph report based on the {question} recommending optimisation and improvements to operations.  Report to be formatted as markdown.',
    tools=[search_tool, transactions_tool, products_tool, customers_tool, planogram_tool, stores_tool, recommendations_tool],
    agent=data_analyst,
    async_execution=False,
    output_file='improvement2-report.md'  # Example of output customization
)

from crewai import Crew, Process

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[researcher, data_analyst],
    tasks=[research_task, data_analysis_task],
    process=Process.sequential,  # Optional: Sequential task execution is default
    manager_llm='gpt-4',
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'question': 'Do you see any patterns in the store data that will help store planners predict future patterns?'})
print(result)