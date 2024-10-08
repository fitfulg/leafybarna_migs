import json
from database_utils import connect_to_db, insert_data, safe_serialize, parse_date

conn = connect_to_db()
cursor = conn.cursor()

with open('OD_Arbrat_Viari_BCN.json', 'r', encoding='utf-8') as f:
    try:
        with conn:
            with cursor:
                query = """
                    INSERT INTO local_street_trees 
                    (codi, adreca, nom_cientific, nom_castella, nom_catala, categoria_arbrat, 
                     tipus_reg, nom_barri, codi_districte, nom_districte, catalogacio, data_plantacio)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """

                for line in f:
                    try:
                        data = json.loads(line)

                        required_fields = [
                            'codi', 'adreca', 'nom_cientific', 'nom_castella', 'nom_catala', 
                            'categoria_arbrat', 'tipus_reg', 'nom_barri', 'codi_districte', 
                            'nom_districte', 'catalogacio', 'data_plantacio'
                        ]

                        missing_fields = [field for field in required_fields if field not in data]
                        if missing_fields:
                            print(f"Skipping record: missing fields {missing_fields}")
                            continue

                        for key in data:
                            data[key] = safe_serialize(data[key])

                        data_plantacio = parse_date(data.get('data_plantacio'))

                        insert_data(cursor, query, (
                            data['codi'],
                            data['adreca'],
                            data['nom_cientific'],
                            data['nom_castella'],
                            data['nom_catala'],
                            data['categoria_arbrat'],
                            data['tipus_reg'],
                            data['nom_barri'],
                            int(data['codi_districte']) if data.get('codi_districte') else None,
                            data['nom_districte'],
                            data['catalogacio'],
                            data_plantacio
                        ))

                        print(f"Rows affected: {cursor.rowcount}")

                    except json.JSONDecodeError:
                        print(f"Error decoding JSON on line: {line}")
                    except KeyError as e:
                        print(f"Missing key: {e}")
                    except Exception as e:
                        print(f"Insert error: {e}")

            conn.commit()
            print("Data committed successfully.")

    except Exception as e:
        print(f"Migration error: {str(e)}")

cursor.close()
conn.close()

print("Migration completed.")
