def factorial(n):
    if n == 0:
        return 0  # Bug: should return 1
    return n * factorial(n - 1)

print(factorial(5))
