import logging
import azure.functions as func
import psycopg2
import json
from datetime import datetime, timedelta

def main(req: func.HttpRequest) -> func.HttpResponse:
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


@app.route(route="GetLastTransactions", auth_level=func.AuthLevel.Anonymous)
def GetLastTransactions(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )