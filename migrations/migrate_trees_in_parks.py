import requests
from database_utils import connect_to_db, insert_data, safe_serialize, parse_date

conn = connect_to_db()
cursor = conn.cursor()

url = 'https://opendata-ajuntament.barcelona.cat/resources/bcn/Arbrat/OD_Arbrat_Parcs_BCN.json'

response = requests.get(url)
data = response.json()

print(f"Data structure example: {data[0] if len(data) > 0 else 'No data'}")

query = """
    INSERT INTO trees_in_parks 
    (codi, nom_cientific, nom_castella, nom_catala, adreca, tipus_reg, 
     data_plantacio, x_etrs89, y_etrs89, latitud, longitud, nom_parc, 
     codi_barri, nom_barri, codi_districte, nom_districte, espai_verd, 
     catalogacio, tipus_element, categoria_arbrat, cat_especie_id, tipus_aigua)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

try:
    with conn:
        with cursor:
            for tree in data:
                print(f"Processing tree data: {tree}")
                
                codi = tree.get('codi', 'Unknown')
                nom_cientific = safe_serialize(tree.get('nom_cientific', 'Unknown'))
                nom_castella = safe_serialize(tree.get('nom_castella', 'Unknown'))
                nom_catala = safe_serialize(tree.get('nom_catala', 'Unknown'))
                adreca = safe_serialize(tree.get('adreca', 'Unknown'))
                tipus_reg = safe_serialize(tree.get('tipus_reg', 'Unknown'))
                data_plantacio = parse_date(tree.get('data_plantacio'))
                x_etrs89 = tree.get('x_etrs89')
                y_etrs89 = tree.get('y_etrs89')
                latitud = tree.get('latitud')
                longitud = tree.get('longitud')
                nom_parc = safe_serialize(tree.get('nom_parc', 'Unknown'))
                codi_barri = tree.get('codi_barri')
                nom_barri = safe_serialize(tree.get('nom_barri', 'Unknown'))
                codi_districte = tree.get('codi_districte')
                nom_districte = safe_serialize(tree.get('nom_districte', 'Unknown'))
                espai_verd = safe_serialize(tree.get('espai_verd', 'Unknown'))
                catalogacio = safe_serialize(tree.get('catalogacio', 'Unknown'))
                tipus_element = safe_serialize(tree.get('tipus_element', 'Unknown'))
                categoria_arbrat = safe_serialize(tree.get('categoria_arbrat', 'Unknown'))
                cat_especie_id = tree.get('cat_especie_id')
                tipus_aigua = safe_serialize(tree.get('tipus_aigua', 'Unknown'))

                insert_data(cursor, query, (
                    codi, nom_cientific, nom_castella, nom_catala, adreca, tipus_reg,
                    data_plantacio, x_etrs89, y_etrs89, latitud, longitud, nom_parc,
                    codi_barri, nom_barri, codi_districte, nom_districte, espai_verd,
                    catalogacio, tipus_element, categoria_arbrat, cat_especie_id, tipus_aigua
                ))

                print(f"Inserted tree: {codi}")

        conn.commit()
        print("Data committed successfully.")

except Exception as e:
    print(f"Error during migration: {str(e)}")

cursor.close()
conn.close()

print("Data migration process completed.")
