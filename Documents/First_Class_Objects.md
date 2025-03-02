# First Class Objects

In Python, first-class objects (also known as first-class citizens) are entities that can be passed around as arguments, returned from functions, modified, and assigned to variables. The concept of first-class objects is fundamental to many programming languages,

Example:

### 1 - Assign to a Variable:

we define a function greet that takes a name as an argument and returns a greeting. We then assign this function to a new variable greet_func. Now, greet_func can be used just like greet.

![image](https://github.com/user-attachments/assets/4ef4d573-6fe8-4394-ac5f-49d7d190a193)

```
def greet(name):
    return f"Hello, {name}!"

greet_func = greet
print(greet_func("Alice"))  # Output: Hello, Alice!
```

### 2 - Pass as an Argument: Functions can be passed as arguments to other functions.

In this example, the greet function takes another function (func) as an argument and calls it with the string "Hello, World!". Depending on whether shout or whisper is passed to greet, the output will be in uppercase or lowercase, respectively.

![image](https://github.com/user-attachments/assets/8579e586-d1dc-4258-895a-f8e2cbd2fa11)

```
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    return func("Hello, World!")

print(greet(shout))  # Output: HELLO, WORLD!
print(greet(whisper))  # Output: hello, world!
```

### 3 - Pass as an Argument: Functions can be passed as arguments to other functions.

Here, create_multiplier is a function that returns another function multiplier. The multiplier function takes a single argument y and multiplies it by x. When create_multiplier(2) is called, it returns a new function that multiplies any given value by 2.

![image](https://github.com/user-attachments/assets/5e6fed58-3cf8-40f1-97c8-a8918df42a3b)

```
def create_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

double = create_multiplier(2)
print(double(5))  # Output: 10
```

### 4 - Store in Data Structures: Functions can be stored in data structures like lists and dictionaries.

In this example, we store the add and subtract functions in a dictionary operations. By referencing the dictionary keys, we can dynamically call the stored functions.

![image](https://github.com/user-attachments/assets/bb66b89b-7ac8-44db-a245-e9969b51ecc6)

```
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
```

### 5 - Modify and Extend at Runtime: Functions and other objects can be modified or extended at runtime.

Here, the greet function is initially defined to return a standard greeting. Later, we redefine greet to point to excited_greet, which returns a more enthusiastic greeting. This shows that functions can be reassigned to different implementations during the program's execution.

![image](https://github.com/user-attachments/assets/0c51ed52-dde1-4fb8-8708-9a2f2496e2d0)

```
def greet(name):
    return f"Hello, {name}!"

def excited_greet(name):
    return f"HELLO, {name}!!!"

greet = excited_greet
print(greet("Bob"))  # Output: HELLO, BOB!!!
```

