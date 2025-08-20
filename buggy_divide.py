def divide(a, b):
    if b == 0:
        return 'Error: Division by zero'
    return a / b  # Bug fixed: now divides

print(divide(8, 2))
