
In Python, variables and constants are both used to store data, but they have different purposes and conventions.

## Variable

Variables are used to store data that can change throughout the execution of a program. You can assign a value to a variable and later change it if needed.

Each system work with different variable. For Example:
- customer registration: client name, address etc
- Personal: age, name, size, etc
- Bank: account valor, account balance etc 

### Example Practice Variable:

```
# Number Variable:
age = 25
print(age)  # Output: 25

age = 30
print(age)  # Output: 30

# String Variable:
name = "Alice"
print(name)  # Output: Alice

name = "Bob"
print(name)  # Output: Bob

# List Variable:
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Dictionary Variable:
person = {"name": "Alice", "age": 25}
print(person)  # Output: {'name': 'Alice', 'age': 25}

person["age"] = 26
print(person)  # Output: {'name': 'Alice', 'age': 26}

# Boolean Variable:
is_active = True
print(is_active)  # Output: True

is_active = False
print(is_active)  # Output: False
```


## Constant

Constants, on the other hand, are used to store data that should not change once it is set. While Python does not have built-in support for constants (like some other programming languages).

Each system work with different variable. For Example:
- STATE_NAME: São Paulo, Texas...
- CITY_NAME: Chicago, Rio de Janeiro...
- WEEK_NAME: Sunday, Saturday...

### Example Practice Constant:

```
# Mathematical Constant:
PI = 3.14159
print(PI)  # Output: 3.14159

# It is discouraged to change the value of a constant
# PI = 3.14
# print(PI)  # Output: 3.14

# Gravity Constant:
GRAVITY = 9.81
print(GRAVITY)  # Output: 9.81

# Speed of Light:
SPEED_OF_LIGHT = 299792458  # in meters per second
print(SPEED_OF_LIGHT)  # Output: 299792458

# Planck's Constant:
PLANCK_CONSTANT = 6.62607015e-34  # in Joules per second
print(PLANCK_CONSTANT)  # Output: 6.62607015e-34
```

