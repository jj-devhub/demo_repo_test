def celsius_to_fahrenheit(celsius):
    # Bug fixed: correct formula C * 9/5 + 32
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    # Bug fixed: correct order of operations (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"212°F = {fahrenheit_to_celsius(212)}°C")
