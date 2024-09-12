import sys
import os
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'migrations')))

from database_utils import connect_to_db
from datetime import datetime

conn = connect_to_db()
cursor = conn.cursor()

output_dir = 'static'
os.makedirs(output_dir, exist_ok=True)

def fetch_db_dates(table_name, date_column):
    query = f"SELECT DISTINCT {date_column} FROM {table_name} WHERE {date_column} IS NOT NULL"
    cursor.execute(query)
    return sorted([str(row[0]) for row in cursor.fetchall()])

def read_csv_dates(file_name):
    file_path = os.path.join(output_dir, file_name)
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        return sorted([row[0] for row in reader])

def save_to_csv(dates, file_name):
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w') as file:
        file.write("date\n")
        for date in dates:
            file.write(f"{date}\n")
    print(f"Dates saved in{file_path}")

def compare_dates(csv_dates, db_dates):
    new_dates = [date for date in db_dates if date not in csv_dates]
    removed_dates = [date for date in csv_dates if date not in db_dates]
    
    if new_dates:
        print(f"New dates found: {new_dates}")
    if removed_dates:
        print(f"Deleted dates: {removed_dates}")
    
    if not new_dates and not removed_dates:
        print("No changes were detected.")

def detect_updates():
    print("\nScanning 'local_interest_trees':")
    csv_dates = read_csv_dates('localInterestTrees_created.csv')
    db_dates = fetch_db_dates('local_interest_trees', 'created')
    compare_dates(csv_dates, db_dates)
    save_to_csv(db_dates, 'localInterestTrees_created.csv')

    print("\nScanning 'local_street_trees':")
    csv_dates = read_csv_dates('localStreetTrees_fechas.csv')
    db_dates = fetch_db_dates('local_street_trees', 'data_plantacio')
    compare_dates(csv_dates, db_dates)
    save_to_csv(db_dates, 'localStreetTrees_fechas.csv')

    print("\nScanning 'parks_and_gardens':")
    csv_dates = read_csv_dates('parksAndGardens_created_dates.csv')
    db_dates = fetch_db_dates('parks_and_gardens', 'created')
    compare_dates(csv_dates, db_dates)
    save_to_csv(db_dates, 'parksAndGardens_created_dates.csv')

    print("\nScanning 'trees_in_parks':")
    csv_dates = read_csv_dates('treesInParks_fechas.csv')
    db_dates = fetch_db_dates('trees_in_parks', 'data_plantacio')
    compare_dates(csv_dates, db_dates)
    save_to_csv(db_dates, 'treesInParks_fechas.csv')

if __name__ == '__main__':
    detect_updates()

cursor.close()
conn.close()
