import os
import psycopg2
import json

# Connection parameters
host = 'cprpostgres-db.postgres.database.azure.com'
database = 'cprcashier'
username = 'cpradmin'
password = 'Apr1l2024'

print("Current working directory:", os.getcwd())

# Path to your JSON file
file_path = 'all-products.json'

# Open the file and load the JSON data
with open(file_path, 'r') as file:
    data = json.load(file)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=host,
    database=database,
    user=username,
    password=password
)

# Cursor to perform database operations
cur = conn.cursor()

# Create the 'planovision' table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS planovision (
        id SERIAL PRIMARY KEY,
        category VARCHAR(255),
        product_name VARCHAR(255),
        position VARCHAR(255),
        product_id INT,
        FOREIGN KEY (product_id) REFERENCES products (id)
    );
""")

# Insert data into the 'planovision' table
for category in data['categories']:
    cat_name = category['category']
    for product in category['products']:
        product_name = product['name']
        position = product['position']
        
        # Fetch the product ID assuming product names are unique
        cur.execute("SELECT id FROM products WHERE name = %s;", (product_name,))
        result = cur.fetchone()  # Fetch once and store the result
        if result:
            product_id = result[0]
            cur.execute("""
                INSERT INTO planovision (category, product_name, position, product_id)
                VALUES (%s, %s, %s, %s);
            """, (cat_name, product_name, position, product_id))
        else:
            print(f"Product not found: {product_name}")  # Optional: to track which products aren't found

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()
