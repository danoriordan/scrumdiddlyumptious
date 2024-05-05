import os

os.environ["SERPER_API_KEY"] = "991f5608e25ea4cbb4c7b958e8b5c0adbd1bf262"  # serper.dev API key
os.environ["OPENAI_API_KEY"] = "sk-proj-S9aYVQCFpMb9gdZee0EVT3BlbkFJ2C1vFeXNXwtwmLmoB8d6"
db_uri="""postgresql://cpradmin:Apr1l2024@cprpostgres-db.postgres.database.azure.com:5432/cprcashier"""
#planovision_test="""https://planovision-apim.azure-api.net/productrecognition/ms-pretrained-product-detection/runs/test1"""

from crewai import Agent
from crewai_tools import SerperDevTool
from crewai_tools import PGSearchTool
from crewai import Task
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase


llm = ChatOpenAI(model="gpt-4", temperature=0)


db = SQLDatabase.from_uri(db_uri)
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM products LIMIT 10;")

# Initialize the tool with the database URI and the target table name
#my_tool = PGSearchTool(db_uri=db_uri, table_name='transactions', verbose=True, memory=True, cache=True, max_rpm=100, share_crew=True, allow_delegation=True, backstory="You are a sql database expert with a passion for analyzing data")
transactions_tool = PGSearchTool(db_uri=db_uri, table_name='transactions')
products_tool = PGSearchTool(db_uri=db_uri, table_name='products')
customers_tool = PGSearchTool(db_uri=db_uri, table_name='customers')
planogram_tool = PGSearchTool(db_uri=db_uri, table_name='planogram')
stores_tool = PGSearchTool(db_uri=db_uri, table_name='stores')
recommendations_tool = PGSearchTool(db_uri=db_uri, table_name='recommendations')
planovision_tool = PGSearchTool(db_uri=db_uri, table_name='planovision')

search_tool = SerperDevTool() # To do a search on the internet

# Creating a senior analyst agent with memory and verbose mode
manager = Agent(
    role='Senior Manager',
    goal='Your main job is to answer the {question} giving a detailed response',
    verbose=True,
    memory=True,
    backstory=(
        "You are the main supervisor agent finalizing and approving analysis from your worker agents"
        "We want you to give detailed reasoning on why you have come to any conclusions"
    ),
    allow_delegation=True
)

# Creating a transactions agent with custom tools and delegation capability
data_analyst = Agent(
    role='Transactions',
    goal='Based on the {question} retrieve and analyse relevant data for your manager_agent to build the final response',
    verbose=True,
    memory=True,
    backstory=(
        "You are a sql and json expert with a passion for analyzing data"
    ),

    tools=[transactions_tool, products_tool, customers_tool, stores_tool],
    allow_delegation=True
)

# Enterprise Data Analysis task
enterprise_data_task = Task(
    description=(
        "Your task is to be an expert on the backend systems that manage all your stores data"
    ),
    expected_output='Well formatted data from the {question}. The data to be formatted as json.',
    tools=[products_tool, transactions_tool, customers_tool, stores_tool],
    agent=data_analyst
)

# Recommendations task with language model configuration
report_generation_task = Task(
    description=(
        "Your task is to analyse the data coming from the Enterprise Data Analysis task"
    ),
    expected_output='A report based on the work done enterprise_data_task. The report to be formatted as markdown.',
    tools=[],
    agent=manager,
    async_execution=False,
    output_file='planovision-report.md',
    output_parser=GuardrailsOutputParser()
)

from crewai import Crew, Process

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents=[manager, data_analyst],
    tasks=[enterprise_data_task, report_generation_task],
    process=Process.sequential,  # Optional: Sequential task execution is default
    manager_llm=llm,
    memory=False,
    cache=False,
    max_rpm=100,
    share_crew=True,
    verbose=True,
    output_log_file='planovision-report.log'
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'question': 'What products are doing well in the stores?'})
print(result)