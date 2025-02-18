
# Old Sytle

name = "Alice"
age = 30

greeting = "Hello, %s! You are %d years old. Again name is %s." % (name, age, name)
print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.


# Format 01

name = "Alice"
age = 30

greeting = "Hello, {}! You are {} years old. Again name is {}.".format(name, age, name)
print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.

# Format 02 - inform position
name = "Alice"
age = 30

greeting = "Hello, {0}! You are {1} years old. Again name is {0}.".format(name, age)
print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.


# Format 03 - Declare variable
name = "Alice"
age = 30
greeting = "Hello, {name}! You are {age} years old. Again name is {name}".format(name=name, age=age)
print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.


# Format 04 - Dictionary

dados = {"name": "Alice", "age": 30}

greeting = "Hello, {name}! You are {age} years old. Again name is {name}".format(**dados)
print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.


# f String
name = "Alice"
age = 30

greeting = f"Hello, {name}! You are {age} years old. Again name is {name}."
print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.