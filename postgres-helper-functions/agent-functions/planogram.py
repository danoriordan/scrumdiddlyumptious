import json
import decimal
import psycopg2
from datetime import datetime

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return super(DecimalEncoder, self).default(obj)

def get_planogram_rows(num, host, database, username, password):
    """
    Fetches a specified number of rows from the 'planogram' table in a PostgreSQL database and returns them as a JSON string.

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

    # Select the specified number of rows from the 'planogram' table
    cur.execute(f"SELECT * FROM planogram LIMIT {num};")
    rows = cur.fetchall()

    # Get column names
    column_names = [desc[0] for desc in cur.description]

    # Convert rows to dictionaries for JSON serialization
    rows_json = [dict(zip(column_names, row)) for row in rows]

    # Close the cursor and connection
    cur.close()
    conn.close()

    # Return the rows as a JSON string
    return json.dumps(rows_json, indent=2, cls=DecimalEncoder)

# Example usage of the function
#print(get_planogram_rows(10, 'your-db-host', 'your-db-name', 'your-db-username', 'your-db-password'))
print(get_planogram_rows(10, 'cprpostgres-db.postgres.database.azure.com', 'cprcashier', 'cpradmin', 'Apr1l2024'))
