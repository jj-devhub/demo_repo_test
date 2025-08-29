def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Bug fixed: removed extra +1

print(fibonacci(6))
