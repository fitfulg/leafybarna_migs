from flask import request
from flask import jsonify
from data_fetcher import fetch_data

def apply_filters(data, filters):
    """Apply filters to the data based on query parameters."""
    print("Filters to apply:", filters)
    print("Data length before filtering:", len(data))

    for key, value in filters.items():
        if value:
            print(f"Filtering by {key} with value {value}")
            for item in data:
                print(f"Actual value of catalogacio in data: {item.get(key, '')}")
            data = [item for item in data if value.lower() in str(item.get(key, '')).lower()]

    print("Data length after filtering:", len(data))
    return data


def get_generic_filters(filter_keys):
    """Retrieve filters based on the provided keys from query parameters."""
    filters = {}
    for key in filter_keys:
        filters[key] = request.args.get(key)
    return filters

def get_unique_values_for_key(source_info, key):
    """Generic function to return unique values for a specified key from a dataset."""
    data = fetch_data(source_info["source"], source_info["type"])
    unique_values = {item.get(key, '').strip() for item in data if key in item and item.get(key)}
    return jsonify(list(unique_values))