# 1 - Assign to a Variable:

def greet(name):
    return f"Hello, {name}!"

greet_func = greet
print(greet_func("Alice"))  # Output: Hello, Alice!


# 2 - Pass as an Argument: Functions can be passed as arguments to other functions.

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    return func("Hello, World!")

print(greet(shout))  # Output: HELLO, WORLD!
print(greet(whisper))  # Output: hello, world!

# 3 - Pass as an Argument: Functions can be passed as arguments to other functions.


def create_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

double = create_multiplier(2)
print(double(5))  # Output: 10


# 4 - Store in Data Structures: Functions can be stored in data structures like lists and dictionaries.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

operations = {
    "add": add,
    "subtract": subtract
}
print(operations["add"](10, 5))  # Output: 15
print(operations["subtract"](10, 5))  # Output: 5


# 5 - Modify and Extend at Runtime: Functions and other objects can be modified or extended at runtime.

def greet(name):
    return f"Hello, {name}!"

def excited_greet(name):
    return f"HELLO, {name}!!!"

greet = excited_greet
print(greet("Bob"))  # Output: HELLO, BOB!!!