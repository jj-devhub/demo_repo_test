import time

# Memoization cache for fibonacci
fib_cache = {}

def fibonacci_recursive(n):
    # Bug fixed: added memoization for efficiency
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n in fib_cache:
        return fib_cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    fib_cache[n] = result
    return result

def calculate_execution_time(func, arg):
    # Bug fixed: handle exceptions in the function
    start_time = time.time()
    try:
        result = func(arg)
        end_time = time.time()
        return result, end_time - start_time
    except Exception as e:
        end_time = time.time()
        return f"Error: {e}", end_time - start_time

# This will be much faster now with memoization
print("Calculating fibonacci(35)...")
result, exec_time = calculate_execution_time(fibonacci_recursive, 35)
print(f"Result: {result}, Time: {exec_time:.4f} seconds")

# This will handle the exception gracefully
print("Calculating fibonacci(-5)...")
result2, exec_time2 = calculate_execution_time(fibonacci_recursive, -5)
print(f"Result: {result2}, Time: {exec_time2:.4f} seconds")
