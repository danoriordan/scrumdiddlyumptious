import psycopg2
from psycopg2 import sql

# Connection parameters
host = 'cprpostgres-db.postgres.database.azure.com'
database = 'cprcashier'
username = 'cpradmin'
password = 'Apr1l2024'

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    database=database,
    user=username,
    password=password
)

# Cursor to perform database operations
cur = conn.cursor()

# SQL command to create the table if it doesn't exist
create_table_command = sql.SQL("""
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(100),
    brand VARCHAR(100),
    price NUMERIC(6,2),
    unit INT
)
""")

# Data to insert
products = [
    ('Cheerios', 'Cereal', 'General Mills', 3.99, 40),
    ('Cheerios Honey Nut', 'Cereal', 'General Mills', 4.29, 42),
    ('Wheaties', 'Cereal', 'General Mills', 4.49, 38),
    ('Chex', 'Cereal', 'General Mills', 3.89, 36),
    ('Crispix', 'Cereal', 'Kellogg’s', 3.99, 34),
    ('Cracklin Oat Bran', 'Cereal', 'Kellogg’s', 4.99, 38),
    ('Life', 'Cereal', 'Quaker', 4.49, 32),
    ('Giant Size Cheerios', 'Cereal', 'General Mills', 5.49, 55),
    ('Warheads Extreme Sour', 'Candy', 'Warheads', 1.99, 20),
    ('Swedish Fish', 'Candy', 'Swedish Fish', 1.89, 18),
    ('Sour Patch Kids', 'Candy', 'Sour Patch', 1.99, 15),
    ('Haribo Gold-Bears', 'Candy', 'Haribo', 1.79, 22),
    ('Mike and Ike', 'Candy', 'Mike and Ike', 1.69, 14),
    ('Tostitos Original', 'Chips', 'Tostitos', 2.99, 10),
    ('Tostitos Party Size Original', 'Chips', 'Tostitos', 4.99, 18),
    ('Doritos Nacho Cheese Party Size', 'Chips', 'Doritos', 4.99, 18),
    ('Doritos Cool Ranch Party Size', 'Chips', 'Doritos', 4.99, 18),
    ('Doritos Cool Ranch', 'Chips', 'Doritos', 3.49, 12),
    ('Tostitos Scoops', 'Chips', 'Tostitos', 3.29, 14),
    ('Simply Orange Mango', 'Juice', 'Simply Beverages', 2.99, 52),
    ('Tropicana Orange No Pulp', 'Juice', 'Tropicana', 3.29, 59),
    ('Del Monte Guava Mango', 'Juice', 'Del Monte', 3.09, 47),
    ('Farmstand Strawberry Banana', 'Juice', 'Farmstand', 3.79, 52),
    ('Oasis Smoothie Strawberry Banana', 'Juice', 'Oasis', 2.89, 46),
    ('Fruitopia Strawberry Passion Awareness', 'Juice', 'Fruitopia', 2.59, 50),
    ('Simply Grapefruit', 'Juice', 'Simply Beverages', 3.29, 48),
    ('Tropicana Orange Tangerine', 'Juice', 'Tropicana', 3.49, 52)
]

# SQL command for deleting existing data
delete_command = sql.SQL("DELETE FROM products")

# SQL command for inserting data
insert_command = sql.SQL("INSERT INTO products (name, category, brand, price, unit) VALUES (%s, %s, %s, %s, %s)")

# Execute the commands and commit the changes
try:
    # Create the table if it does not exist
    cur.execute(create_table_command)
    # Delete existing products
    cur.execute(delete_command)
    # Insert new products
    for product in products:
        cur.execute(insert_command, product)
    conn.commit()
except Exception as e:
    print("An error occurred:", e)
    conn.rollback()
finally:
    # Close the communication with the database
    cur.close()
    conn.close()
