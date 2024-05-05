import psycopg2

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

# List of missing products with assumed category, brand, and estimated price
products = [
    ("Cracklin' Oat Bran", 'Cereal', 'Kellogg’s', 4.99, 40),
    ("Del Monte Premium Orange", 'Juice', 'Del Monte', 3.50, 50),
    ("Oasis Health Break Antioxia", 'Juice', 'Oasis', 3.75, 45),
    ("Oasis Health Break Berry Pomegranate", 'Juice', 'Oasis', 3.75, 45),
    ("Tostitos Cantina Traditional", 'Chips', 'Tostitos', 3.25, 30),
    ("Doritos Spicy Nacho", 'Chips', 'Doritos', 3.49, 40),
    ("Doritos Nacho Cheese", 'Chips', 'Doritos', 3.49, 40),
    ("Doritos Flamas", 'Chips', 'Doritos', 3.49, 40),
    ("Body Rox", 'Candy', 'Generic', 2.99, 30),
    ("Mentos Fruit", 'Candy', 'Mentos', 1.29, 50),
    ("Twizzlers", 'Candy', 'Hershey’s', 2.49, 70),
    ("Lemonhead", 'Candy', 'Ferrara', 0.99, 40),
    ("Nerds", 'Candy', 'Wonka', 1.49, 45),
    ("Tic Tac", 'Candy', 'Ferrero', 1.19, 30),
    ("Jelly Belly", 'Candy', 'Jelly Belly', 2.99, 50),
    ("Hot Tamales", 'Candy', 'Just Born', 1.89, 45),
    ("Skittles", 'Candy', 'Wrigley', 1.99, 40),
    ("Starburst", 'Candy', 'Wrigley', 1.99, 40)
]

# SQL command for inserting data
insert_command = "INSERT INTO products (name, category, brand, price, unit) VALUES (%s, %s, %s, %s, %s)"

# Execute the command and commit the changes
try:
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

print("Products inserted successfully.")
