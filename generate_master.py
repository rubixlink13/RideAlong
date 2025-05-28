import json
import requests

def get_client(file_name : str) -> str:
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
            return data['id'], data['secret']
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_name}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file: {file_name}")
        return None
    except KeyError as e:
        print(f"Error: Invalid key: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
