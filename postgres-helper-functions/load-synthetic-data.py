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

def load_transactions_data(cur, num_rows):
    """
    This function generates and loads synthetic data into the transactions table.

    Parameters:
    cur (psycopg2.extensions.cursor): The cursor object.
    num_rows (int): The number of rows to generate and load.
    """

    fake = Faker()

    # Drop table if it exists otherwise create the table
    cur.execute("DROP TABLE IF EXISTS transactions;")
    cur.execute("""
        CREATE TABLE transactions (
            transaction_id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL,
            customer_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity INT NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            store_id INT NOT NULL,
            payment_method VARCHAR(50),
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
            FOREIGN KEY (product_id) REFERENCES products (product_id),
            FOREIGN KEY (store_id) REFERENCES stores (store_id)
        );
""")
    
    # Create a table to store the synthetic data
    for _ in range(num_rows):
        timestamp = fake.date_time_this_year()
        customer_id = random.randint(1, 100)  # Assuming you have customers with IDs 1-100
        product_id = random.randint(1, 100)  # Assuming you have products with IDs 1-100
        quantity = random.randint(1, 10)
        amount = round(random.uniform(1, 100), 2)  # Random price between 1 and 100
        store_id = random.randint(1, 10)  # Assuming you have stores with IDs 1-10
        payment_method = random.choice(['Cash', 'Credit Card', 'Debit Card', 'Mobile Payment'])

        cur.execute("""
            INSERT INTO transactions (timestamp, customer_id, product_id, quantity, amount, store_id, payment_method)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (timestamp, customer_id, product_id, quantity, amount, store_id, payment_method))

# Usage:
load_transactions_data(cur, 100)
conn.commit()

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