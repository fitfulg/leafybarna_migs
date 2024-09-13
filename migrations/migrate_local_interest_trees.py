import requests
import json
import logging
from database_utils import connect_to_db, insert_data, safe_serialize, parse_date, record_exists
from psycopg2 import IntegrityError

logging.basicConfig(filename='tree_processing.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

conn = connect_to_db()
conn.autocommit = False
cursor = conn.cursor()

url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/7052709e-1087-4ef3-862a-1a6c3e9a7200/resource/7ffcae4a-5b1f-4d2e-8b3e-2659ba521736/download'
response = requests.get(url)
data = response.json()

insert_query = """
    INSERT INTO local_interest_trees 
    (register_id, prefix, suffix, name, created, modified, status, status_name,
     core_type, core_type_name, body, tickets_data, addresses, entity_types_data,
     attribute_categories, values, classifications_data, secondary_filters_data,
     geo_epgs_25831, geo_epgs_23031, geo_epgs_4326_latlon, image_data, gallery_data)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (register_id) DO UPDATE SET
    prefix = EXCLUDED.prefix, suffix = EXCLUDED.suffix, name = EXCLUDED.name, created = EXCLUDED.created, 
    modified = EXCLUDED.modified, status = EXCLUDED.status, status_name = EXCLUDED.status_name, 
    core_type = EXCLUDED.core_type, core_type_name = EXCLUDED.core_type_name, body = EXCLUDED.body, 
    tickets_data = EXCLUDED.tickets_data, addresses = EXCLUDED.addresses, entity_types_data = EXCLUDED.entity_types_data,
    attribute_categories = EXCLUDED.attribute_categories, values = EXCLUDED.values, 
    classifications_data = EXCLUDED.classifications_data, secondary_filters_data = EXCLUDED.secondary_filters_data,
    geo_epgs_25831 = EXCLUDED.geo_epgs_25831, geo_epgs_23031 = EXCLUDED.geo_epgs_23031, 
    geo_epgs_4326_latlon = EXCLUDED.geo_epgs_4326_latlon, image_data = EXCLUDED.image_data, 
    gallery_data = EXCLUDED.gallery_data
"""

log_inserts = {
    'success': 0,
    'updated': 0,
    'errors': []
}

def filter_tree_data(tree):
    def safe_parse_date(date_str):
        if isinstance(date_str, str):
            return date_str
        elif date_str:
            return date_str.strftime('%Y-%m-%d %H:%M:%S')
        return None
    
    return {
        'register_id': tree.get('register_id'),
        'prefix': safe_serialize(tree.get('prefix')),
        'suffix': safe_serialize(tree.get('suffix')),
        'name': safe_serialize(tree.get('name', 'Unknown')),
        'created': safe_parse_date(tree.get('created')),
        'modified': safe_parse_date(tree.get('modified')),
        'status': safe_serialize(tree.get('status')),
        'status_name': safe_serialize(tree.get('status_name')),
        'core_type': safe_serialize(tree.get('core_type')),
        'core_type_name': safe_serialize(tree.get('core_type_name')),
        'body': safe_serialize(tree.get('body')),
        'tickets_data': json.dumps(tree.get('tickets_data', [])),
        'addresses': json.dumps(tree.get('addresses', [])),
        'entity_types_data': json.dumps(tree.get('entity_types_data', [])),
        'attribute_categories': json.dumps(tree.get('attribute_categories', [])),
        'values': json.dumps(tree.get('values', [])),
        'classifications_data': json.dumps(tree.get('classifications_data', [])),
        'secondary_filters_data': json.dumps(tree.get('secondary_filters_data', [])),
        'geo_epgs_25831': json.dumps(tree.get('geo_epgs_25831', {})),
        'geo_epgs_23031': json.dumps(tree.get('geo_epgs_23031', {})),
        'geo_epgs_4326_latlon': json.dumps(tree.get('geo_epgs_4326_latlon', {})),
        'image_data': json.dumps(tree.get('image_data', {})),
        'gallery_data': json.dumps(tree.get('gallery_data', []))
    }

try:
    for tree in data:
        try:
            tree_data = filter_tree_data(tree)
            values_to_insert = tuple(tree_data.values())
            
            placeholders_count = insert_query.count('%s')
            logging.debug(f"Valores a insertar (len={len(values_to_insert)}): {values_to_insert}")
            logging.debug(f"Placeholders en la consulta (len={placeholders_count})")

            if len(values_to_insert) != placeholders_count:
                raise ValueError(f"El número de valores no coincide con los placeholders en la consulta SQL. "
                                 f"Placeholders: {placeholders_count}, Valores: {len(values_to_insert)}")

            # Insert or update using ON CONFLICT so we can handle duplicates
            cursor.execute(insert_query, values_to_insert)
            log_inserts['success'] += 1
            logging.info(f"Procesado: {tree_data['name']}")

        except IntegrityError as db_error:
            log_inserts['errors'].append({
                'tree': tree.get('name', 'Unknown'),
                'error': str(db_error),
            })
            logging.error(f"Error en BD para {tree.get('name', 'Unknown')}: {str(db_error)}")
        except Exception as tree_error:
            log_inserts['errors'].append({
                'tree': tree.get('name', 'Unknown'),
                'error': str(tree_error),
            })
            logging.error(f"Error al procesar {tree.get('name', 'Unknown')}: {str(tree_error)}")

    conn.commit()
except Exception as insert_error:
    conn.rollback()
    logging.error(f"Error general: {str(insert_error)}")

finally:
    cursor.close()
    conn.close()

logging.info("\n*** RESULTS ***")
logging.info(f"Inserted/Updated successfully: {log_inserts['success']}")
logging.info(f"Total errors: {len(log_inserts['errors'])}")

if log_inserts['errors']:
    logging.info("\n*** ERRORS ***")
    for error in log_inserts['errors']:
        logging.error(f"Tree: {error['tree']} - Error: {error['error']}")
