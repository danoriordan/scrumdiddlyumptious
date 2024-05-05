import getpass
import os
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool


def enterprise_sql(question: str):
    """
    You are a PostgreSQL expert. Given an input question, first create a syntactically correct PostgreSQL query to run, then look at the results of the query and return the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most 5 results using the LIMIT clause as per PostgreSQL. You can order the results to return the most informative data in the database.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in double quotes (") to denote them as delimited identifiers.
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
    Pay attention to use CURRENT_DATE function to get the current date, if the question involves "today".

    Use the following format:

    Question: {question}
    SQLQuery: SQL Query to run
    SQLResult: Result of the SQLQuery
    Answer: Final answer here

    Only use the following tables:
    {table_info}

    Question: {question}   
    """
    #os.environ["OPENAI_API_KEY"] = getpass.getpass()
    os.environ["OPENAI_API_KEY"] = "sk-proj-S9aYVQCFpMb9gdZee0EVT3BlbkFJ2C1vFeXNXwtwmLmoB8d6"
    db_uri="""postgresql://cpradmin:Apr1l2024@cprpostgres-db.postgres.database.azure.com:5432/cprcashier"""

    db = SQLDatabase.from_uri(db_uri)
    
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    execute_query = QuerySQLDataBaseTool(db=db)
    write_query = create_sql_query_chain(llm, db)
    chain = write_query | execute_query
    response = chain.invoke({"question": question})
    return response

print(enterprise_sql("Can you tell me return the names of the top three customers who have spent the most in the stores"))