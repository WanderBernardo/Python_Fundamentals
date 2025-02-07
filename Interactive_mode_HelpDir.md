
### Document
- https://wiki.python.org.br/ModoInterativo
- https://docs.python.org/3.13/tutorial/interpreter.html


## Interactive Mode

Interactive mode in Python refers to the use of the Python interpreter in a way that allows you to enter and execute Python code line-by-line. This is different from running a script where the entire code is executed at once. 

Interactive mode is very useful for testing snippets of code, experimenting with Python features, and debugging.

There are two way:

Open "New Terminal":
![image](https://github.com/user-attachments/assets/74a68e20-5a34-49ea-9107-0476be739e09)

1 - Type ``` python ``` and press "Enter":
![image](https://github.com/user-attachments/assets/ba442e46-b6bd-4543-b9e6-9020e97f5920)

2 - Type ``` python -i ``` and press "Enter":
![image](https://github.com/user-attachments/assets/01329deb-748d-4fc1-95cc-b00a281497ec)

To leave this mode, type: ``` exit() ```, valid for both forms:
![image](https://github.com/user-attachments/assets/b33fa185-d344-4a86-8432-01cea47ede85)

Case, you will want clear screen, use command  ``` clear ```:

Before:
![image](https://github.com/user-attachments/assets/67c6487f-f752-434a-b0a4-0e3c9333b816)

After:
![image](https://github.com/user-attachments/assets/42d634f7-ecab-47c2-8f3d-bed974b9bd18)


## Command: Help

In Python's interactive mode, the help() function is incredibly useful for getting information about Python modules, classes, functions, and more.

Here's how you can use it:

1 - Use ``` help() ``` and press "Enter":

Enable "Help" mode, it will show a description.
![image](https://github.com/user-attachments/assets/1b3ff86a-2aea-4bd6-a4e5-1cdf72f5845e)

Now, type your doubt, Examplo:
- Command: "print"
- Module: "math"
- Class: "datetime"
- Function: "sorted"

Screen below: type "print" and press "Enter":
![image](https://github.com/user-attachments/assets/82acdd20-23bb-454f-8125-01f345c947a0)

2 - Use ``` help("type here doubt") ``` and press "Enter":
![image](https://github.com/user-attachments/assets/e8c90bb7-478e-4f2e-8e7e-e2e3fed0d5e8)

To leave of help mode. Use command: ``` exit ```. But, you continue in interative mode:
![image](https://github.com/user-attachments/assets/c63dbc26-408b-4a9b-bb27-765cda54dba5)

Look, case you need seach more about: Modulo, class, etc, it will need necessary first "import"(according to the examples below)

### Example practice - Help:
```
# Help on a Specific Object: You can get help on a specific object, such as a function or a module. For example:
>>> help(print)

# Information on a Module: Let's use the math module as an example.
>>> import math
>>> help(math)

# Information on a Class: Let's use the datetime module and its date class.
>>> import datetime
>>> help(datetime.date)

# Information on a Function: Let's use the sorted function as an example.
>>> help(sorted)
```

## Command: Dir

I think it explain better is demostration: How it will be in the "Excel"?

![image](https://github.com/user-attachments/assets/9bc7904c-5bb5-4650-9b97-a15c5a164b96)

Dir = Listing attributes and methods of a built-in, modulo object it possible receive.

1 - Use ``` dir() ``` and press "Enter":
![image](https://github.com/user-attachments/assets/9f80ef29-17b9-457f-8a1d-bdff5a42f809)

2 - Use ``` dir("Specific modulo") ``` and press "Enter":
![image](https://github.com/user-attachments/assets/d6c60f5a-1768-4770-b057-96c488d02e76)

Look, case you need seach more about: Modulo, class, etc, it will need necessary first "import"(according to the examples below)

### Example practice - Help:
```
# Listing attributes and methods of a built-in object:
>>> dir(str)

# Listing attributes and methods of a module:
>>> import math
>>> dir(math)

# Listing attributes and methods of an instance:
>>> class Example:
...     def __init__(self, x):
...         self.x = x
...     def display(self):
...         print(self.x)
...
>>> example = Example(10)
>>> dir(example)

# Using dir() without arguments:
>>> dir()
```

## Return principal Menu

https://github.com/WanderBernardo/Python_Fundamentals
