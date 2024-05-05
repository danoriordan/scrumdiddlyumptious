import random
from faker import Faker
import psycopg2
from datetime import datetime, timedelta

# Faker settings
fake = Faker()

# PostgreSQL connection settings
host = 'cprpostgres-db.postgres.database.azure.com'
database = 'cprcashier'
username = 'cpradmin'
password = 'Apr1l2024'

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    database=database,
    user=username,
    password=password
)

# Create a cursor object
cur = conn.cursor()

def load_synthetic_data_stores(cur, num_rows):
    """
    This function generates and loads synthetic data into the stores table.

    Parameters:
    cur (psycopg2.extensions.cursor): The cursor object.
    num_rows (int): The number of rows to generate and load.
    """
    # Drop table if it exists otherwise create the table
    cur.execute("DROP TABLE IF EXISTS stores;")
    cur.execute("""
        CREATE TABLE stores (
            store_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            location VARCHAR(100),
            manager VARCHAR(100),
            chain_id INT,
            region VARCHAR(50)
        );
""")
    
    fake = Faker()

    for _ in range(num_rows):
        name = fake.company()
        location = fake.city()
        manager = fake.name()
        chain_id = random.randint(1, 10)  # Assuming you have chain IDs between 1 and 10
        region = fake.state()

        cur.execute("""
            INSERT INTO stores (name, location, manager, chain_id, region)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, location, manager, chain_id, region))

# Usage:
load_synthetic_data_stores(cur, 100)
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()