# Function with Args and Kwargs

Case is necessary include any arguments in the function, use "ARGs" and "KWARGs". Because it's simple and easy.


### Args

Allows you to pass a variable number of non-keyword arguments to a function. The arguments are collected in a tuple.

**Example:**

![image](https://github.com/user-attachments/assets/ea109006-600b-4fa9-8967-a91f67824897)

```
def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3)
```

### Kwargs

Allows you to pass a variable number of keyword arguments to a function. The arguments are collected in a dictionary.

**Example:**

![image](https://github.com/user-attachments/assets/3305b50b-0232-46ae-a346-0309e2d381c7)


```
def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(name="Alice", age=25)

```

### Argument, Args and Kwargs

![image](https://github.com/user-attachments/assets/81e3d582-2bab-4136-b04d-3343739aeaaa)

```
def example_function(data, *args, **kwargs):
    for arg in args:
        print(arg)
    for data, name, age in kwargs.items():
        print(f"{data}:{key}: {value}")

example_function("02/15/2025, "1, 2, 3, name="Alice", age=25)
```

Use words: ARGs and KWARGs are Good Practice. But it can use other words. Try!!!
