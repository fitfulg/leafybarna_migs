import requests
from database_utils import connect_to_db, insert_data, safe_serialize, parse_date, record_exists

conn = connect_to_db()
conn.autocommit = True
cursor = conn.cursor()

log_inserts = {
    'success': 0,
    'updated': 0,
    'failed': [],
    'errors': []
}

url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/5d43ed16-f93a-442f-8853-4bf2191b2d39/resource/b42797a8-3be7-4504-ad7c-12174de222de/download'

response = requests.get(url)
data = response.json()

insert_query = """
    INSERT INTO parks_and_gardens 
    (register_id, prefix, suffix, name, created, modified, status, status_name,
     core_type, core_type_name, body, tickets_data, addresses, entity_types_data,
     classifications_data, secondary_filters_data, geo_epgs_25831, geo_epgs_23031, 
     geo_epgs_4326_latlon, sections_data, image_data)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

update_query = """
    UPDATE parks_and_gardens SET
    prefix = %s, suffix = %s, name = %s, created = %s, modified = %s, status = %s, status_name = %s,
    core_type = %s, core_type_name = %s, body = %s, tickets_data = %s, addresses = %s,
    entity_types_data = %s, classifications_data = %s, secondary_filters_data = %s, geo_epgs_25831 = %s,
    geo_epgs_23031 = %s, geo_epgs_4326_latlon = %s, sections_data = %s, image_data = %s
    WHERE register_id = %s
"""

try:
    for park in data:
        register_id = park.get('register_id')
        if record_exists(cursor, "parks_and_gardens", register_id):
            cursor.execute(update_query, (
                safe_serialize(park.get('prefix')), safe_serialize(park.get('suffix')), safe_serialize(park.get('name', 'Unknown')), 
                parse_date(park.get('created')), parse_date(park.get('modified')), safe_serialize(park.get('status')), 
                safe_serialize(park.get('status_name')), safe_serialize(park.get('core_type')), safe_serialize(park.get('core_type_name')), 
                safe_serialize(park.get('body')), safe_serialize(park.get('tickets_data', [])), safe_serialize(park.get('addresses', [])), 
                safe_serialize(park.get('entity_types_data', [])), safe_serialize(park.get('classifications_data', [])), 
                safe_serialize(park.get('secondary_filters_data', [])), safe_serialize(park.get('geo_epgs_25831')), 
                safe_serialize(park.get('geo_epgs_23031')), safe_serialize(park.get('geo_epgs_4326_latlon')), 
                safe_serialize(park.get('sections_data', [])), safe_serialize(park.get('image_data', {})), 
                register_id
            ))
            log_inserts['updated'] += 1
        else:
            cursor.execute(insert_query, (
                register_id, safe_serialize(park.get('prefix')), safe_serialize(park.get('suffix')), safe_serialize(park.get('name', 'Unknown')), 
                parse_date(park.get('created')), parse_date(park.get('modified')), safe_serialize(park.get('status')), 
                safe_serialize(park.get('status_name')), safe_serialize(park.get('core_type')), safe_serialize(park.get('core_type_name')), 
                safe_serialize(park.get('body')), safe_serialize(park.get('tickets_data', [])), safe_serialize(park.get('addresses', [])), 
                safe_serialize(park.get('entity_types_data', [])), safe_serialize(park.get('classifications_data', [])), 
                safe_serialize(park.get('secondary_filters_data', [])), safe_serialize(park.get('geo_epgs_25831')), 
                safe_serialize(park.get('geo_epgs_23031')), safe_serialize(park.get('geo_epgs_4326_latlon')), 
                safe_serialize(park.get('sections_data', [])), safe_serialize(park.get('image_data', {}))
            ))
            log_inserts['success'] += 1

except Exception as e:
    log_inserts['errors'].append(str(e))

finally:
    cursor.close()
    conn.close()

print(f"Successful inserts: {log_inserts['success']}")
print(f"Successful updates: {log_inserts['updated']}")
print(f"Errors: {log_inserts['errors']}")
