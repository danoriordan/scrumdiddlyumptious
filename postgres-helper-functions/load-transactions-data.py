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

    # Drop table if it exists and then recreate it
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
            FOREIGN KEY (product_id) REFERENCES products (id),
            FOREIGN KEY (store_id) REFERENCES stores (store_id)
        );
    """)
    
    # Fetch product prices from the products table
    cur.execute("SELECT id, price FROM products;")
    products_prices = cur.fetchall()
    products_price_dict = {product_id: price for product_id, price in products_prices}

    # Create synthetic transaction data
    for _ in range(num_rows):
        timestamp = fake.date_time_this_year()
        customer_id = random.randint(1, 100)  # Assuming you have customers with IDs 1-100
        product_id, price = random.choice(products_prices)
        quantity = random.randint(1, 10)
        amount = price * quantity
        store_id = random.randint(1, 10)  # Assuming you have stores with IDs 1-10
        payment_method = random.choice(['Cash', 'Credit Card', 'Debit Card', 'Mobile Payment'])

        cur.execute("""
            INSERT INTO transactions (timestamp, customer_id, product_id, quantity, amount, store_id, payment_method)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (timestamp, customer_id, product_id, quantity, amount, store_id, payment_method))

# Usage:
load_transactions_data(cur, 200)
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
