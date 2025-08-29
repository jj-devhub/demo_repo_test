import json
import pickle
from collections import defaultdict
import copy

def serialize_data(data, format_type):
    # Bug fixed: handle unsupported formats and serialization errors
    try:
        if format_type == "json":
            return json.dumps(data, default=str)  # Handle non-serializable objects
        elif format_type == "pickle":
            return pickle.dumps(data)
        else:
            raise ValueError(f"Unsupported format: {format_type}")
    except (TypeError, ValueError) as e:
        raise ValueError(f"Serialization failed: {e}")

def deserialize_data(data, format_type):
    # Bug fixed: add error handling for corrupted data
    try:
        if format_type == "json":
            return json.loads(data)
        elif format_type == "pickle":
            return pickle.loads(data)
        else:
            raise ValueError(f"Unsupported format: {format_type}")
    except (json.JSONDecodeError, pickle.UnpicklingError, ValueError) as e:
        raise ValueError(f"Deserialization failed: {e}")

def deep_merge_dicts(dict1, dict2):
    # Bug fixed: don't modify original dictionary
    result = copy.deepcopy(dict1)
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def group_by_property(items, property_name, default_group="no_property"):
    # Bug fixed: handle missing properties gracefully
    groups = defaultdict(list)
    for item in items:
        try:
            if isinstance(item, dict):
                group_key = item.get(property_name, default_group)
            else:
                group_key = getattr(item, property_name, default_group)
            groups[group_key].append(item)
        except (KeyError, AttributeError):
            groups[default_group].append(item)
    return dict(groups)

def flatten_nested_list(nested_list, max_depth=None):
    # Bug fixed: handle deeply nested structures and non-list items
    def _flatten_recursive(item, current_depth=0):
        if max_depth is not None and current_depth >= max_depth:
            return [item]
        
        if isinstance(item, (list, tuple)):
            flattened = []
            for sub_item in item:
                flattened.extend(_flatten_recursive(sub_item, current_depth + 1))
            return flattened
        else:
            return [item]
    
    return _flatten_recursive(nested_list)

# Test improved scenarios
class CustomClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"CustomClass({self.value})"

# This will now work with JSON using default=str
custom_obj = CustomClass(42)
try:
    serialized = serialize_data(custom_obj, "json")
    print(f"Serialized: {serialized}")
    
    # Test with dict containing custom object
    complex_data = {"obj": custom_obj, "number": 123}
    serialized_complex = serialize_data(complex_data, "json")
    print(f"Complex serialized: {serialized_complex}")
except Exception as e:
    print(f"Serialization error: {e}")

# This won't modify original dict
original_dict = {"a": 1, "nested": {"x": 1}}
other_dict = {"b": 2, "nested": {"y": 2}}
merged = deep_merge_dicts(original_dict, other_dict)
print(f"Original unchanged: {original_dict}")
print(f"Merged result: {merged}")

# This will handle missing property gracefully
items = [{"name": "Alice", "age": 30}, {"name": "Bob"}]
try:
    grouped = group_by_property(items, "age", "unknown_age")
    print(f"Grouped with defaults: {grouped}")
except Exception as e:
    print(f"Grouping error: {e}")

# This will handle deep nesting properly
nested = [1, [2, [3, 4]], 5]
print(f"Fully flattened: {flatten_nested_list(nested)}")
print(f"Limited depth flattened: {flatten_nested_list(nested, max_depth=2)}")

# Test error handling
try:
    bad_json = '{"incomplete": '
    deserialize_data(bad_json, "json")
except ValueError as e:
    print(f"Deserialization error handled: {e}")
