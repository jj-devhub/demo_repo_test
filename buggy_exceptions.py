def risky_division(a, b):
    # Bug fixed: add proper exception handling
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        return result
    except TypeError:
        raise TypeError("Both arguments must be numbers")

def process_numbers(numbers):
    results = []
    for i, num in enumerate(numbers):
        try:
            # Bug fixed: handle invalid data types gracefully
            if num is None:
                continue  # Skip None values
            result = float(num) * 2 + 10
            results.append(result)
        except (TypeError, ValueError) as e:
            print(f"Warning: Skipping invalid value at index {i}: {num} ({e})")
            continue
    return results

def read_config_value(config, key, default=None):
    # Bug fixed: handle missing keys and provide defaults
    try:
        if key not in config:
            if default is not None:
                return default
            raise KeyError(f"Configuration key '{key}' not found")
        
        value = config[key]
        if isinstance(value, dict) and 'value' in value:
            return value['value']
        return value
    except (KeyError, TypeError) as e:
        if default is not None:
            return default
        raise

def unsafe_file_operation(filename):
    # Bug fixed: use context manager for proper file handling
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Processing inside context manager ensures file is closed
            processed = content.upper()
            return processed
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except IOError as e:
        raise IOError(f"Error reading file '{filename}': {e}")

def parse_date_string(date_str, formats=None):
    # Bug fixed: support multiple formats and proper error handling
    from datetime import datetime
    
    if formats is None:
        formats = ['%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y', '%d/%m/%Y']
    
    for date_format in formats:
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse date '{date_str}' with any of the supported formats: {formats}")

# Test cases with proper error handling
try:
    print(risky_division(10, 0))  # Handled gracefully
except ValueError as e:
    print(f"Division error: {e}")

try:
    numbers = [1, 2, "three", 4, None]
    result = process_numbers(numbers)  # Skips invalid values
    print(f"Processed numbers: {result}")
except Exception as e:
    print(f"Processing error: {e}")

try:
    config = {"database": {"host": "localhost"}}
    value = read_config_value(config, "nonexistent", "default_value")
    print(f"Config value: {value}")
except Exception as e:
    print(f"Config error: {e}")

try:
    date_obj = parse_date_string("2023/12/25")  # Multiple formats supported
    print(f"Parsed date: {date_obj}")
except ValueError as e:
    print(f"Date parsing error: {e}")
