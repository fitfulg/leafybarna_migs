import requests
import pandas as pd
import json
import os

def fetch_data(source, source_type='url'):
    """Fetch data either from a URL or a local file."""
    try:
        if source_type == 'url':
            response = requests.get(source)
            response.raise_for_status()
            return response.json()
        elif source_type == 'local_json':
            # Read the entire JSON file (if it's a standard JSON)
            with open(source, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        elif source_type == 'local_jsonl':
            # Read a JSONL file line by line
            data = []
            with open(source, 'r', encoding='utf-8') as json_file:
                for line in json_file:
                    data.append(json.loads(line))
            return data
        elif source_type == 'csv':
            csv_data = pd.read_csv(source)
            return csv_data.to_json(orient='records')
        else:
            raise ValueError("Unsupported source type")
    except Exception as e:
        raise Exception(f"Failed to fetch data from {source}: {str(e)}")
