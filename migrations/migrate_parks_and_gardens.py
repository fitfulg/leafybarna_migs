import json
import requests
from database_utils import connect_to_db
from datetime import datetime

conn = connect_to_db()
conn.autocommit = True
cursor = conn.cursor()

log_inserts = {
    'success': 0,
    'updated': 0,
    'failed': [],
    'errors': []
}

def parse_date(date_string):
    try:
        return datetime.fromisoformat(date_string.replace("Z", "+00:00")) if date_string else None
    except ValueError:
        return None  # Return None if date is invalid

# Serialize complex data types and handle null values
def safe_serialize(data):
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

def record_exists(register_id):
    cursor.execute("SELECT 1 FROM parks_and_gardens WHERE register_id = %s", (register_id,))
    return cursor.fetchone() is not None

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
        try:
            register_id = park.get('register_id')
            prefix = safe_serialize(park.get('prefix'))
            suffix = safe_serialize(park.get('suffix'))
            name = safe_serialize(park.get('name', 'Unknown'))
            created = parse_date(park.get('created'))
            modified = parse_date(park.get('modified'))
            status = safe_serialize(park.get('status'))
            status_name = safe_serialize(park.get('status_name'))
            core_type = safe_serialize(park.get('core_type'))
            core_type_name = safe_serialize(park.get('core_type_name'))
            body = safe_serialize(park.get('body'))

            # Serialize complex data types
            tickets_data = safe_serialize(park.get('tickets_data', []))
            addresses = safe_serialize(park.get('addresses', []))
            entity_types_data = safe_serialize(park.get('entity_types_data', []))
            classifications_data = safe_serialize(park.get('classifications_data', []))
            secondary_filters_data = safe_serialize(park.get('secondary_filters_data', []))

            # Extract and serialize geo data
            geo_epgs_25831 = safe_serialize(park.get('geo_epgs_25831'))
            geo_epgs_23031 = safe_serialize(park.get('geo_epgs_23031'))
            geo_epgs_4326_latlon = safe_serialize(park.get('geo_epgs_4326_latlon'))

            sections_data = safe_serialize(park.get('sections_data', []))
            image_data = safe_serialize(park.get('image_data', {}))

            if record_exists(register_id):
                cursor.execute(update_query, (
                    prefix, suffix, name, created, modified, status, status_name, core_type, core_type_name, body, 
                    tickets_data, addresses, entity_types_data, classifications_data, secondary_filters_data, 
                    geo_epgs_25831, geo_epgs_23031, geo_epgs_4326_latlon, sections_data, image_data, register_id
                ))
                print(f"Updated park: {name}")
                log_inserts['updated'] += 1
            else:
                cursor.execute(insert_query, (
                    register_id, prefix, suffix, name, created, modified, status, status_name, core_type, 
                    core_type_name, body, tickets_data, addresses, entity_types_data, classifications_data, 
                    secondary_filters_data, geo_epgs_25831, geo_epgs_23031, geo_epgs_4326_latlon, sections_data, image_data
                ))
                print(f"Inserted park: {name}")
                log_inserts['success'] += 1

        except Exception as insert_error:
            log_inserts['errors'].append({
                'park': name,
                'error': str(insert_error),
                'params': park
            })
            print(f"Error processing park {name}: {insert_error}")

finally:
    cursor.close()
    conn.close()

print("\nData migration log:")
print(f"Successful inserts: {log_inserts['success']}")
print(f"Successful updates: {log_inserts['updated']}")
print(f"Failed inserts due to other errors: {len(log_inserts['errors'])}")

for error in log_inserts['errors']:
    print(f"- {error['park']} failed due to {error['error']}")
