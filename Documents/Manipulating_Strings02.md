# Manipulating Strings - Part 01

## Variable Interpolation

Variable interpolation is a feature in programming where variables are directly embedded within strings, allowing for more readable and maintainable code.Instead of manually concatenating strings and variables, interpolation lets you insert variables seamlessly.

In resume: Include vaiable inside of text. This way, it's possible has a text personalized. Example: You need send 100 letters, each a letters different person. So, this way, variable interpolation, change name, address conform parameters.

**Python makes it possible some ways:**

Placeholders in programming are special symbols or sequences that are used within strings to represent variable values that will be inserted later. They make it easier to build strings dynamically.

### 1: Old style %
Include % join with (s,d or f etc) to indicate variable. Example:

![image](https://github.com/user-attachments/assets/cf2a63ae-5e2a-4f71-be2b-2e3dc3d206fc)

Image above, where it would need to be name and age, it was change for "placeholders" (%s and %d) and in the end of the phrase listed the variables.it's necessary each variable conform sequence input in the text. Other point, if in the text there is the same variable. Example: "name", need include again and in order.

**Python (Old-Style String Formatting):**
- %s for strings
- %d for integers
- %f for floating-point numbers

```
name = "Alice"
age = 30
greeting = "Hello, %s! You are %d years old. Again name is %s" % (name, age, name)
print(greeting)  # Output: Hello, Alice! You are 30 years old.
```

**But, this way not indicate more the use. It's complex. Remenber OLD STYLE!**


### 2: Format
It doesn't use "%s","%d"... altered for "{}". No more necessary indicate if the variable is string or integer. But, there is the same problem. It's necessary include variable by variable in the end pharse. Pay Attetion, with position of the variable.

![image](https://github.com/user-attachments/assets/04eebe35-cc1d-4084-98aa-cb0b0152e994)

```
name = "Alice"
age = 30
greeting = "Hello, {}! You are {} years old. Again name is {}".format(name, age, name)
print(greeting)  # Output: Hello, Alice! You are 30 years old.
```

**Others standard inside of the Format:**

- Including the position of the variable. This way, isn't necessary more repet variable in the end pharse:
  ```
  name = "Alice"
  age = 30
  greeting = "Hello, {1}! You are {2} years old. Again name is {1}".format(name, age)
  print(greeting)  # Output: Hello, Alice! You are 30 years old.
  ```

- Pass variable of way appointed. As if it were declarate variable inside text:
  ```
  name = "Alice"
  age = 30
  greeting = "Hello, {name}! You are {age} years old. Again name is {name}".format(name=name, age=age)
  print(greeting)  # Output: Hello, Alice! You are 30 years old.
  ```
  
-  Other possible is create a word dictionary:
  ```
  name = "Alice"
  age = 30
  greeting = "Hello, {name}! You are {age} years old. Again name is {name}".format(**pessoa)
  print(greeting)  # Output: Hello, Alice! You are 30 years old.
  ```

### 3: 













