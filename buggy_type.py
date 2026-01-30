def add_numbers(a, b):
    if isinstance(a, str):
        a = int(a)
    return a + b

print(add_numbers("5", 10))  # Bug fixed: string converted to integer
