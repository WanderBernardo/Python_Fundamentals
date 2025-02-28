# Function with Args and Kwargs

Case is necessary include any arguments in the function, use "ARGs" and "KWARGs". Because it's simple and easy.


### Args

Allows you to pass a variable number of non-keyword arguments to a function. The arguments are collected in a tuple.

**Example:**

```
def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3)
```

### Kwargs

Allows you to pass a variable number of keyword arguments to a function. The arguments are collected in a dictionary.

**Example:**

```
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name="Alice", age=25)

```

### Argument, Args and Kwargs

```
def example_function(data, *args, **kwargs):
    for arg in args:
        print(arg)
    for data, name, age in kwargs.items():
        print(f"{data}:{key}: {value}")

example_function("02/15/2025, "1, 2, 3, name="Alice", age=25)
```
