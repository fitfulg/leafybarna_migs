import requests
from database_utils import connect_to_db, insert_data, safe_serialize, parse_date, record_exists

conn = connect_to_db()
conn.autocommit = True
cursor = conn.cursor()

url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/7052709e-1087-4ef3-862a-1a6c3e9a7200/resource/7ffcae4a-5b1f-4d2e-8b3e-2659ba521736/download'
response = requests.get(url)
data = response.json()

insert_query = """
    INSERT INTO local_interest_trees 
    (register_id, prefix, suffix, name, created, modified, status, status_name,
     core_type, core_type_name, body, tickets_data, addresses, entity_types_data,
     attribute_categories, values, classifications_data, secondary_filters_data,
     geo_epgs_25831, geo_epgs_23031, geo_epgs_4326_latlon, image_data)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

update_query = """
    UPDATE local_interest_trees SET
    prefix = %s, suffix = %s, name = %s, created = %s, modified = %s, status = %s, status_name = %s,
    core_type = %s, core_type_name = %s, body = %s, tickets_data = %s, addresses = %s,
    entity_types_data = %s, attribute_categories = %s, values = %s, classifications_data = %s,
    secondary_filters_data = %s, geo_epgs_25831 = %s, geo_epgs_23031 = %s, geo_epgs_4326_latlon = %s,
    image_data = %s WHERE register_id = %s
"""

log_inserts = {
    'success': 0,
    'updated': 0,
    'failed': [],
    'errors': []
}

try:
    for tree in data:
        register_id = tree.get('register_id')
        prefix = safe_serialize(tree.get('prefix'))
        suffix = safe_serialize(tree.get('suffix'))
        name = safe_serialize(tree.get('name', 'Unknown'))
        created = parse_date(tree.get('created'))
        modified = parse_date(tree.get('modified'))
        # Serialize complex data types
        other_data = {field: safe_serialize(tree.get(field, default)) for field, default in [
            ('status', None), ('status_name', None), ('core_type', None),
            ('core_type_name', None), ('body', None), ('tickets_data', []), ('addresses', []),
            ('entity_types_data', []), ('attribute_categories', []), ('values', []),
            ('classifications_data', []), ('secondary_filters_data', []), ('geo_epgs_25831', None),
            ('geo_epgs_23031', None), ('geo_epgs_4326_latlon', None), ('image_data', {})
        ]}

        if record_exists(cursor, 'local_interest_trees', register_id):
            cursor.execute(update_query, tuple(other_data.values()) + (register_id,))
            log_inserts['updated'] += 1
        else:
            cursor.execute(insert_query, (register_id,) + tuple(other_data.values()))
            log_inserts['success'] += 1

except Exception as insert_error:
    log_inserts['errors'].append({
        'tree': name,
        'error': str(insert_error),
        'params': tree
    })

finally:
    cursor.close()
    conn.close()

print(f"Successful inserts: {log_inserts['success']}")
print(f"Successful updates: {log_inserts['updated']}")
print(f"Errors: {log_inserts['errors']}")
