import sys
import os
import json
import requests
from database_utils import connect_to_db, insert_data

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

conn = connect_to_db()
cursor = conn.cursor()

url = 'https://opendata-ajuntament.barcelona.cat/resources/bcn/Arbrat/OD_Arbrat_Parcs_BCN.json'

response = requests.get(url)
data = response.json()

# Debugging: Print the structure of the data to understand its layout
print(f"Data structure example: {data[0] if len(data) > 0 else 'No data'}")

try:
    with conn:
        with cursor:
            query = """
                INSERT INTO trees_in_parks 
                (codi, nom_cientific, nom_castella, nom_catala, adreca, tipus_reg, 
                 data_plantacio, x_etrs89, y_etrs89, latitud, longitud, nom_parc, 
                 codi_barri, nom_barri, codi_districte, nom_districte, espai_verd, 
                 catalogacio, tipus_element, categoria_arbrat, cat_especie_id, tipus_aigua)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            for tree in data:
                print(f"Processing tree data: {tree}")
                
                try:
                    # Check if required fields are present, otherwise provide defaults
                    codi = tree.get('codi', 'Unknown')
                    nom_cientific = tree.get('nom_cientific', 'Unknown')
                    nom_castella = tree.get('nom_castella', 'Unknown')
                    nom_catala = tree.get('nom_catala', 'Unknown')
                    adreca = tree.get('adreca', 'Unknown')
                    tipus_reg = tree.get('tipus_reg', 'Unknown')
                    data_plantacio = tree.get('data_plantacio') if tree.get('data_plantacio') else None
                    x_etrs89 = float(tree['x_etrs89']) if tree.get('x_etrs89') else None
                    y_etrs89 = float(tree['y_etrs89']) if tree.get('y_etrs89') else None
                    latitud = float(tree['latitud']) if tree.get('latitud') else None
                    longitud = float(tree['longitud']) if tree.get('longitud') else None
                    nom_parc = tree.get('espai_verd', 'Unknown')
                    codi_barri = int(tree['codi_barri']) if tree.get('codi_barri') else None
                    nom_barri = tree.get('nom_barri', 'Unknown')
                    codi_districte = int(tree['codi_districte']) if tree.get('codi_districte') else None
                    nom_districte = tree.get('nom_districte', 'Unknown')
                    espai_verd = tree.get('espai_verd', 'Unknown')
                    catalogacio = tree.get('catalogacio', 'Unknown')
                    tipus_element = tree.get('tipus_element', 'Unknown')
                    categoria_arbrat = tree.get('categoria_arbrat', 'Unknown')
                    cat_especie_id = int(tree['cat_especie_id']) if tree.get('cat_especie_id') else None
                    tipus_aigua = tree.get('tipus_aigua', 'Unknown')

                    # Insert data into the database
                    insert_data(cursor, query, (
                        codi,
                        nom_cientific,
                        nom_castella,
                        nom_catala,
                        adreca,
                        tipus_reg,
                        data_plantacio,
                        x_etrs89,
                        y_etrs89,
                        latitud,
                        longitud,
                        nom_parc,
                        codi_barri,
                        nom_barri,
                        codi_districte,
                        nom_districte,
                        espai_verd,
                        catalogacio,
                        tipus_element,
                        categoria_arbrat,
                        cat_especie_id,
                        tipus_aigua
                    ))

                    print(f"Inserted tree: {codi}")

                except ValueError as ve:
                    print(f"Error with ID conversion: {ve}")
                except Exception as e:
                    print(f"Error inserting tree: {e}")

        conn.commit()
        print("Data committed successfully.")

except Exception as e:
    print(f"Error during migration: {str(e)}")

cursor.close()
conn.close()

print("Data migration process completed.")
