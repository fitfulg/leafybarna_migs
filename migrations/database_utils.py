# database_utils.py

import os
import json
import psycopg2
from datetime import datetime
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

def safe_serialize(data):
    """Serialize data safely to JSON and escape problematic characters."""
    try:
        if isinstance(data, (list, dict)):
            return json.dumps(data)
        elif isinstance(data, str):
            return data.replace('\r\n', '\\n').replace("'", "''")
        elif data is None:
            return None
        else:
            return str(data)
    except TypeError:
        return None

def parse_date(date_string):
    """Parse ISO formatted date string to a datetime object."""
    try:
        return datetime.fromisoformat(date_string.replace("Z", "+00:00")) if date_string else None
    except ValueError:
        return None

def record_exists(cursor, table, register_id):
    """Check if a record exists in the specified table."""
    cursor.execute(f"SELECT 1 FROM {table} WHERE register_id = %s", (register_id,))
    return cursor.fetchone() is not None
