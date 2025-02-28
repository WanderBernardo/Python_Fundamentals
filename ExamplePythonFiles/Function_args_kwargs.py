def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3)


def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name="Alice", age=25)


def example_function(year, *args, **kwargs):
    print(f"{year}: {args}: {kwargs}")

example_function(2025,1, 2, 3, name="Alice", age=25)