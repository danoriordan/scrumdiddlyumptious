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

def load_synthetic_data_customers(cur, num_rows):
    """
    This function generates and loads synthetic data into the customers table.

    Parameters:
    cur (psycopg2.extensions.cursor): The cursor object.
    num_rows (int): The number of rows to generate and load.
    """
    # Drop table if it exists otherwise create the table
    cur.execute("DROP TABLE IF EXISTS customers;")
    cur.execute("""
        CREATE TABLE customers (
            customer_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            gender VARCHAR(10),
            location VARCHAR(100),
            income DECIMAL(12, 2),
            loyalty_status VARCHAR(20)
        );
""")
    fake = Faker()

    for _ in range(num_rows):
        name = fake.name()
        age = random.randint(18, 70)  # Assuming customer age is between 18 and 70
        gender = random.choice(['Male', 'Female'])
        location = fake.city()
        income = round(random.uniform(30000, 100000), 2)  # Random income between 30000 and 100000
        loyalty_status = random.choice(['Bronze', 'Silver', 'Gold', 'Platinum'])

        cur.execute("""
            INSERT INTO customers (name, age, gender, location, income, loyalty_status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, age, gender, location, income, loyalty_status))

# Usage:
load_synthetic_data_customers(cur, 100)
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()