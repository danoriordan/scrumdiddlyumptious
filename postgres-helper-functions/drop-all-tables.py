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


# Drop table if it exists otherwise create the table
cur.execute("DROP TABLE IF EXISTS transactions;")
cur.execute("DROP TABLE IF EXISTS customers;")
cur.execute("DROP TABLE IF EXISTS planogram;")
cur.execute("DROP TABLE IF EXISTS stores;")
cur.execute("DROP TABLE IF EXISTS recommendations;")
cur.execute("DROP TABLE IF EXISTS products;")

conn.commit()


# Close the cursor and connection
cur.close()
conn.close()