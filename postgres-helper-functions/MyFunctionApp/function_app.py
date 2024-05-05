import datetime
import json
import logging
import psycopg2
import azure.functions as func

app = func.FunctionApp()

@app.route(route="GetTransactions", auth_level=func.AuthLevel.Anonymous)
def GetTransactions(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Database connection settings
    host = 'cprpostgres-db.postgres.database.azure.com'
    database = 'cprcashierdb'
    user = 'cpradmin'
    password = 'Apr1l2024'

    # Establish connection to the PostgreSQL database
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cur = conn.cursor()

    # Query to fetch the last 100 transactions
    cur.execute("SELECT * FROM cashier_logs ORDER BY registered_at DESC LIMIT 100")
    records = cur.fetchall()

    # Close the database connection
    cur.close()
    conn.close()

    # Prepare data to return as JSON
    transactions = [
        {"id": record[0], "product_name": record[1], "product_description": record[2], "price": str(record[3]), "quantity": record[4], "registered_at": record[5].isoformat()}
        for record in records
    ]

    return func.HttpResponse(
        json.dumps(transactions),
        mimetype="application/json"
    )