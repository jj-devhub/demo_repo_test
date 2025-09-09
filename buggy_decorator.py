import functools
def log_function_call(func):
    # Bug: decorator does not preserve function signature
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def add(a, b):
    return a + b

@log_function_call
def greet(name):
    return f"Hello, {name}!"

print(add(2, 3))
print(greet("Alice"))
print(add.__name__)  # Bug: should be 'add', but will be 'wrapper'
