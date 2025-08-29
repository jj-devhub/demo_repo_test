import os

def parse_config_file(filename):
    config = {}
    # Bug fixed: added error handling for file operations
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Config file '{filename}' not found")
        
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line or line.startswith('#'):  # Skip empty lines and comments
                    continue
                
                # Bug fixed: handle lines without '=' properly
                if '=' not in line:
                    print(f"Warning: Skipping malformed line {line_num}: {line}")
                    continue
                
                # Bug fixed: handle multiple '=' characters
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                
                # Bug fixed: basic type conversion
                if value.lower() in ('true', 'false'):
                    config[key] = value.lower() == 'true'
                elif value.isdigit():
                    config[key] = int(value)
                elif value.replace('.', '').isdigit():
                    config[key] = float(value)
                else:
                    config[key] = value
                    
    except Exception as e:
        print(f"Error reading config file: {e}")
        return {}
    
    return config

def save_config_file(config, filename):
    # Bug fixed: added error handling for write operations
    try:
        with open(filename, 'w') as file:
            for key, value in config.items():
                # Bug fixed: handle None values and escape special characters
                if value is None:
                    value = ""
                elif isinstance(value, str) and '=' in value:
                    value = f'"{value}"'  # Quote values containing =
                
                file.write(f"{key}={value}\n")
    except Exception as e:
        print(f"Error writing config file: {e}")
        return False
    return True

# Test with a config that doesn't exist
try:
    config = parse_config_file("nonexistent.conf")
    print(config)
except Exception as e:
    print(f"Error: {e}")

# Test with malformed data
malformed_config = {
    "database_host": "localhost",
    "database_port": None,
    "password": "secret=with=equals",
    "debug": True
}

save_config_file(malformed_config, "test.conf")
print("Config saved")
