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

def load_synthetic_data_recommendations(cur, num_rows):
    """
    This function generates and loads synthetic data into the stores table.

    Parameters:
    cur (psycopg2.extensions.cursor): The cursor object.
    num_rows (int): The number of rows to generate and load.
    """
    # Drop table if it exists otherwise create the table
    cur.execute("DROP TABLE IF EXISTS recommendations;")
    cur.execute("""
        CREATE TABLE recommendations (
            recommendation_id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL,
            product_id INT NOT NULL,
            placement VARCHAR(50),
            reason TEXT,
            confidence FLOAT,
            region VARCHAR(50),
            channel VARCHAR(50),
            category VARCHAR(50),
            CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES products (id)
        );
""")
    
    fake = Faker()

    for _ in range(num_rows):
        timestamp = fake.date_time_this_year()
        product_id = random.randint(1, 27)  # Assuming you have products with IDs 1-100
        placement = fake.word(ext_word_list=['Top Left', 'Top Middle', 'Top Right', 'Middle Left', 'Middle Right', 'Middle Middle', 'Bottom Left', 'Bottom Middle', 'Bottom Right'])
        reason = fake.sentence()
        confidence = round(random.uniform(0, 1), 2)  # Random confidence between 0 and 1
        region = fake.state()
        channel = fake.word(ext_word_list=['Web', 'Mobile', 'Email', 'In-Store'])
        category = fake.word(ext_word_list=['Cereal', 'Candy', 'Chips', 'Garden'])

        cur.execute("""
            INSERT INTO recommendations (timestamp, product_id, placement, reason, confidence, region, channel, category)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (timestamp, product_id, placement, reason, confidence, region, channel, category))


# Usage:
load_synthetic_data_recommendations(cur, 100)
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()