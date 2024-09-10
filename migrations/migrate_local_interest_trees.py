import json
import requests
from migrations.database_utils import connect_to_db, insert_data

conn = connect_to_db()
cursor = conn.cursor()

url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/7052709e-1087-4ef3-862a-1a6c3e9a7200/resource/7ffcae4a-5b1f-4d2e-8b3e-2659ba521736/download'

response = requests.get(url)
data = response.json()

try:
    with conn:
        with cursor:
            query = """
                INSERT INTO local_interest_trees 
                (register_id, name, created, modified, status, status_name, core_type, 
                 core_type_name, body, district_name, district_id, neighborhood_name, 
                 neighborhood_id, address_name, zip_code, latitud, longitud)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for tree in data:
                for address in tree['addresses']:
                    district_id = int(address.get('district_id')) if address.get('district_id') else None
                    neighborhood_id = int(address.get('neighborhood_id')) if address.get('neighborhood_id') else None

                    insert_data(cursor, query, (
                        tree.get('register_id'),
                        tree.get('name'),
                        tree.get('created'),
                        tree.get('modified'),
                        tree.get('status'),
                        tree.get('status_name'),
                        tree.get('core_type'),
                        tree.get('core_type_name'),
                        tree.get('body'),
                        address.get('district_name'),
                        district_id,
                        address.get('neighborhood_name'),
                        neighborhood_id,
                        address.get('address_name'),
                        address.get('zip_code'),
                        address['location']['geometries'][0]['coordinates'][1],
                        address['location']['geometries'][0]['coordinates'][0]
                    ))

                    print(f"Inserted tree: {tree.get('name')}")

        conn.commit()
        print("Data committed successfully.")

except Exception as e:
    print(f"Migration error: {str(e)}")

cursor.close()
conn.close()

print("Migration completed.")
