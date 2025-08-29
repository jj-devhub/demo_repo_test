import json
import os

def load_config(filename):
    # Bug fixed: add exception handling for file operations
    try:
        with open(filename, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Config file {filename} not found, using defaults")
        return {}
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {filename}: {e}")
        return {}

def save_data(data, filename):
    # Bug fixed: create directory if it doesn't exist
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")

def process_user_data(users):
    processed = []
    for user in users:
        # Bug fixed: check if 'age' field exists before accessing
        if 'age' in user and user['age'] >= 18:
            if 'name' in user:
                processed.append(user['name'].upper())
        elif 'age' not in user:
            print(f"Warning: User {user.get('name', 'unknown')} has no age field")
    return processed

# These will now handle errors gracefully
try:
    config = load_config('nonexistent.json')
    save_data({'test': 'data'}, 'subdir/output.json')
    users = [{'name': 'Alice'}, {'name': 'Bob', 'age': 25}]
    result = process_user_data(users)
    print(result)
except Exception as e:
    print(f"Error: {e}")
