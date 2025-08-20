def factorial(n):
    result = 1  # Bug fixed: start with 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(6))
 # Minimal change: added a comment
