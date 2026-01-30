def factorial(n):
    if n == 0:
        return 1  # Bug fixed: return 1 for n == 0
    else:
        return n * factorial(n - 1)

print(factorial(5))
