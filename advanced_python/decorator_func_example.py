def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


# Applying the decorator using the @ syntax
@logger
def add(a, b):
    return a + b


# Calling the decorated function
result = add(10, 20)
print("Result:", result)
