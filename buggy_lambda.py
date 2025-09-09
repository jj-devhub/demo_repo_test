numbers = [1, 2, 3, 4, 5]
# Bug fixed: lambda predicate should check for even numbers (x % 2 == 0)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
