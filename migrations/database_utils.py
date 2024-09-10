import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def connect_to_db():
    """Establish connection to PostgreSQL database."""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "leafybarna_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "your_secure_password"),
        host=os.getenv("DB_HOST", "localhost")
    )

def insert_data(cursor, query, data):
    """Generic function to insert data into the database."""
    try:
        cursor.execute(query, data)
        print(f"Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        print(f"Problematic data: {data}")
