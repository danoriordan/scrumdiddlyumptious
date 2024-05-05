import random
import psycopg2
from datetime import datetime, timedelta
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return super(DecimalEncoder, self).default(obj)
    
def get_rows(num, host, database, username, password):
    """
    This function fetches a specified number of rows from a PostgreSQL database and returns them as a JSON string.

    Parameters:
    num (int): The number of rows to fetch.
    host (str): The host of the PostgreSQL database.
    database (str): The name of the database.
    username (str): The username to use for authentication.
    password (str): The password to use for authentication.

    Returns:
    str: A JSON string representing the fetched rows.
    """

    # Create a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=username,
        password=password
    )

    # Create a cursor object
    cur = conn.cursor()

    # Select from a num input the number of rows to be returned
    cur.execute(f"SELECT * FROM cashier_logs LIMIT {num};")
    rows = cur.fetchall()

    # Get column names
    column_names = [desc[0] for desc in cur.description]

    # Convert rows to dictionaries
    rows_json = [dict(zip(column_names, row)) for row in rows]

    # Close the cursor and connection
    cur.close()
    conn.close()

    # Return the rows as a JSON string
    return json.dumps(rows_json, indent=2, cls=DecimalEncoder)

# Usage:
print(get_rows(10, 'cprpostgres-db.postgres.database.azure.com', 'cprcashier', 'cpradmin', 'Apr1l2024'))

  
