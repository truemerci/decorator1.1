def decorator(func):
    def inner(*args, **kwargs):
        print(f"Input: {args}")
        print(func(*args, **kwargs))
    return inner


@decorator
def add(x, y):
    return x + y


add(2, 3)
