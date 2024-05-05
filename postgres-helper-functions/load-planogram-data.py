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

def load_synthetic_data_planogram(cur, num_rows):
    """
    This function generates and loads synthetic data into the products table.

    Parameters:
    cur (psycopg2.extensions.cursor): The cursor object.
    num_rows (int): The number of rows to generate and load.
    """
    # Drop table if it exists otherwise create the table
    cur.execute("DROP TABLE IF EXISTS planogram;")
    cur.execute("""
        CREATE TABLE planogram (
            planogram_id SERIAL PRIMARY KEY,
            store_id INT NOT NULL,
            product_id INT NOT NULL,
            aisle INT NOT NULL,
            shelf INT NOT NULL,
            position VARCHAR(50) NOT NULL,
            level INT NOT NULL,
            facing_count INT,
            CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES products (id),
            CONSTRAINT fk_store_id FOREIGN KEY (store_id) REFERENCES stores (store_id)
        );
""")
    
    fake = Faker()

    for _ in range(num_rows):
        store_id = random.randint(1, 100)  # Assuming you have stores with IDs 1-100
        product_id = random.randint(1, 27)  # Assuming you have products with IDs 1-100
        aisle = random.randint(1, 10)  # Assuming aisles are numbered 1-10
        shelf = random.randint(1, 5)  # Assuming shelves are numbered 1-5
        position = random.choice(['Left', 'Middle', 'Right'])
        level = random.randint(1, 5)  # Assuming levels are numbered 1-5
        facing_count = random.randint(1, 10)  # Assuming facing count is between 1 and 10

        cur.execute("""
            INSERT INTO planogram (store_id, product_id, aisle, shelf, position, level, facing_count)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (store_id, product_id, aisle, shelf, position, level, facing_count))

# Usage:
load_synthetic_data_planogram(cur, 100)
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()