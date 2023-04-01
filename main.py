def decorator(func):
    def inner(*args, **kwargs):
        print(f"Input: {args}")
        result = func(*args, **kwargs)
        return result
    return inner


@decorator
def add(x, y):
    return x + y


print(add(2, 3))
