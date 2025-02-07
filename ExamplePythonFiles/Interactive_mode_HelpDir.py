# FIRST ENABLE INTERATIVE MODE AND COPY and PASTE THERE

# COMMAND HELP

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


# COMMAND DIR

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