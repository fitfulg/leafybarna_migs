import json
import requests
from migrations.database_utils import connect_to_db, insert_data

conn = connect_to_db()
cursor = conn.cursor()

url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/5d43ed16-f93a-442f-8853-4bf2191b2d39/resource/b42797a8-3be7-4504-ad7c-12174de222de/download'

response = requests.get(url)
data = response.json()

try:
    with conn:
        with cursor:
            query = """
                INSERT INTO parks_and_gardens 
                (register_id, name, created, modified, status, status_name, 
                 core_type, core_type_name, district_name, district_id, 
                 neighborhood_name, neighborhood_id, address_name, zip_code, 
                 latitud, longitud)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for park in data:
                for address in park['addresses']:
                    try:
                        district_id = int(address.get('district_id')) if address.get('district_id') else None
                        neighborhood_id = int(address.get('neighborhood_id')) if address.get('neighborhood_id') else None

                        insert_data(cursor, query, (
                            park.get('register_id'),
                            park.get('name'),
                            park.get('created'),
                            park.get('modified'),
                            park.get('status'),
                            park.get('status_name'),
                            park.get('core_type'),
                            park.get('core_type_name'),
                            address.get('district_name'),
                            district_id,
                            address.get('neighborhood_name'),
                            neighborhood_id,
                            address.get('address_name'),
                            address.get('zip_code'),
                            address['location']['geometries'][0]['coordinates'][1],  # latitud
                            address['location']['geometries'][0]['coordinates'][0]   # longitud
                        ))

                        print(f"Inserted park: {park.get('name')}")

                    except ValueError as ve:
                        print(f"Error with ID conversion: {ve}")
                    except Exception as e:
                        print(f"Error inserting park: {e}")

        conn.commit()
        print("Data committed successfully.")

except Exception as e:
    print(f"Error during migration: {str(e)}")

cursor.close()
conn.close()

print("Data migration process completed.")
