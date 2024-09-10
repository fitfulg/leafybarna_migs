import os
from flask import jsonify, request
from cache import is_cache_valid, update_cache
from data_fetcher import fetch_data
from utils import apply_filters, get_generic_filters, get_unique_values_for_key

# Define data sources
DATA_SOURCES = {
    "trees_in_parks": {
        "source": "https://opendata-ajuntament.barcelona.cat/resources/bcn/Arbrat/OD_Arbrat_Parcs_BCN.json",
        "type": "url"
    },
    "local_street_trees": {
        # Ruta corregida para el archivo JSON local
        "source": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'OD_Arbrat_Viari_BCN.json'),
        "type": "local_jsonl"
    },
    "parks_and_gardens": {
        "source": "https://opendata-ajuntament.barcelona.cat/data/dataset/5d43ed16-f93a-442f-8853-4bf2191b2d39/resource/b42797a8-3be7-4504-ad7c-12174de222de/download",
        "type": "url"
    },
    "local_interest_trees": {
        "source": "https://opendata-ajuntament.barcelona.cat/data/dataset/7052709e-1087-4ef3-862a-1a6c3e9a7200/resource/7ffcae4a-5b1f-4d2e-8b3e-2659ba521736/download",
        "type": "url"
    }
}

FILTER_KEYS = {
    "trees_in_parks": ['codi_districte', 'nom_cientific', 'categoria_arbrat', 'adreca', 'nom_barri', 'tipus_reg', 'data_plantacio'],
    "local_street_trees": ['codi_districte', 'nom_cientific', 'adreca', 'nom_barri', 'tipus_reg', 'data_plantacio', 'catalogacio'],
}

def get_local_street_trees_source():
    """Get the source for local street trees using the correct static path."""
    # Usamos la ruta correcta sin current_app
    source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'OD_Arbrat_Viari_BCN.json')
    return {
        "source": source_path,
        "type": "local_jsonl"
    }

def handle_data_request(cache_key, source_info, filter_keys):
    """Generic handler for fetching and returning data with caching."""
    cached_data = is_cache_valid(cache_key)
    if cached_data:
        return jsonify(cached_data)

    try:
        data = fetch_data(source_info["source"], source_info["type"])
        
        # Apply pagination if required
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 100))
        start = (page - 1) * per_page
        end = start + per_page
        paginated_data = data[start:end]

        # Retrieve and apply filters dynamically based on filter keys
        filters = get_generic_filters(filter_keys)
        filtered_data = apply_filters(paginated_data, filters)

        # Cache and return filtered data
        update_cache(cache_key, filtered_data)
        return jsonify(filtered_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# TREES IN PARKS
def get_trees_in_parks():
    return handle_data_request("trees_in_parks", DATA_SOURCES["trees_in_parks"], FILTER_KEYS["trees_in_parks"])

def get_trees_in_parks_unique_neighborhoods():
    """Return all unique neighborhood values from the trees-in-parks dataset."""
    return get_unique_values_for_key(DATA_SOURCES["trees_in_parks"], 'nom_barri')

# LOCAL STREET TREES
def get_local_street_trees():
    local_street_trees_source = get_local_street_trees_source()
    return handle_data_request("local_street_trees", local_street_trees_source, FILTER_KEYS["local_street_trees"])

def get_local_street_trees_unique_catalogation():
    """Return all unique catalogation values from the local-street-trees dataset."""
    local_street_trees_source = get_local_street_trees_source()
    return get_unique_values_for_key(local_street_trees_source, 'catalogacio')

# PARKS AND GARDENS
def get_parks_and_gardens():
    return handle_data_request("parks_and_gardens", DATA_SOURCES["parks_and_gardens"], [])

# LOCAL INTEREST TREES
def get_local_interest_trees():
    return handle_data_request("local_interest_trees", DATA_SOURCES["local_interest_trees"], [])
