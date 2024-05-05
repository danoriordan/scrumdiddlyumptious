import os
from embedchain.pipeline import Pipeline as App
from embedchain.loaders.postgres import PostgresLoader

os.environ["OPENAI_API_KEY"] = "sk-proj-S9aYVQCFpMb9gdZee0EVT3BlbkFJ2C1vFeXNXwtwmLmoB8d6"

config = {
    "host": "cprpostgres-db.postgres.database.azure.com",
    "port": "5432",
    "dbname": "cprcashier",
    "user": "cpradmin",
    "password": "Apr1l2024",
}

postgres_loader = PostgresLoader(config=config)


app = App()


app.add("SELECT * FROM transactions;", data_type='postgres', loader=postgres_loader)
app.add("SELECT * FROM customers;", data_type='postgres', loader=postgres_loader)
app.add("SELECT * FROM products;", data_type='postgres', loader=postgres_loader)
app.add("SELECT * FROM planogram;", data_type='postgres', loader=postgres_loader)
app.add("SELECT * FROM stores;", data_type='postgres', loader=postgres_loader)
app.add("SELECT * FROM recommendations;", data_type='postgres', loader=postgres_loader)


#question = "Can you give me a list of the last 20 transactions and the names of the customers for each transaction and the product they bought"
question = "Give me a list of all transcations with transaction_id less than 20"
response = app.query(question)
print(response)

question = "Give me a list of the latest recommendations"
response = app.query(question)
print(response)


