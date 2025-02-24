# Variable Interpolation

Variable interpolation is a feature in programming where variables are directly embedded within strings, allowing for more readable and maintainable code.Instead of manually concatenating strings and variables, interpolation lets you insert variables seamlessly.

In resume: Include vaiable inside of text. This way, it's possible has a text personalized. Example: You need send 100 letters, each a letters different person. So, this way, variable interpolation, change name, address conform parameters.

**Python makes it possible some ways:**

Placeholders in programming are special symbols or sequences that are used within strings to represent variable values that will be inserted later. They make it easier to build strings dynamically.

**Pay Attetion in the structure**

### 1: Old style %
Include % join with (s,d or f etc) to indicate variable. Example:

![image](https://github.com/user-attachments/assets/3d23d11a-4a54-4845-86e1-201df7d009eb)

Image above, where it would need to be name and age, it was change for "placeholders" (%s and %d) and in the end of the phrase listed the variables.it's necessary each variable conform sequence input in the text. Other point, if in the text there is the same variable. Example: "name", need include again and in order.

**Python (Old-Style String Formatting):**
- %s for strings
- %d for integers
- %f for floating-point numbers

```
name = "Alice"
age = 30
greeting = "Hello, %s! You are %d years old. Again name is %s" % (name, age, name)
print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.
```

**But, this way not indicate more the use. It's complex. Remenber OLD STYLE!**


### 2: Format
It doesn't use "%s","%d"... altered for "{}". No more necessary indicate if the variable is string or integer. But, there is the same problem. It's necessary include variable by variable in the end pharse. Pay Attetion, with position of the variable.

![image](https://github.com/user-attachments/assets/ff2b0ffe-7dfe-4f93-91cc-091ffafef5c5)

```
name = "Alice"
age = 30
greeting = "Hello, {}! You are {} years old. Again name is {}.".format(name, age, name)
print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.
```

**Others standard inside of the Format:**

- Including the position of the variable. This way, isn't necessary more repet variable in the end pharse:

  ![image](https://github.com/user-attachments/assets/cda58533-a53d-4b1a-b864-e5cf68a11d37)

  ```
  name = "Alice"
  age = 30
  greeting = "Hello, {0}! You are {2} years old. Again name is {0}".format(name, age)
  print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.
  ```

  In this case, position start in zero (0).
  
- Pass variable of way appointed. As if it were declarate variable inside text:

  ![image](https://github.com/user-attachments/assets/6ebb055f-df42-4931-b9c9-0745fc4442bc)

  ```
  name = "Alice"
  age = 30
  greeting = "Hello, {name}! You are {age} years old. Again name is {name}".format(name=name, age=age)
  print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.
  ```
  
- Other possible is create a word dictionary:

  ![image](https://github.com/user-attachments/assets/b7eedcb5-d8d3-49e6-b1d3-59d012e09235)

  ```
  name = "Alice"
  age = 30
  greeting = "Hello, {name}! You are {age} years old. Again name is {name}".format(**pessoa)
  print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.
  ```

### 3: f-string:

It's similar with "Format". But, with improvements. It isn't necessary include the variable in the end of the text.

Start with "f" and hability the use variable in the text.

![image](https://github.com/user-attachments/assets/8259290b-1e61-42aa-8ddd-d78b1638ca25)

This way is better and normally used.

```
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old. Again name is {name}."
print(greeting)  # Output: Hello, Alice! You are 30 years old. Again name is Alice.
```

### F-string to decimal number

Case, you will be working with decimal number. Example: 10.2345678. But you need only two number after dot.

Structure: **{"variable name":."amount after of the dot"F}**

```
PI = 3.14159
print(f"Valor de PI: {PI:.2f}" # "Valor de PI: 3.14"
```


Case you want include space before variable inform amount.

Structure: **{"variable name":""amount of space before of space"."amount after of the dot"F}**

```
PI = 3.14159
print(f"Valor de PI: {PI:10.2f}") # "Valor de PI:       3.14"
```

![image](https://github.com/user-attachments/assets/6ace44db-1636-47f6-b460-ec3d2cc51222)




Now, download file and try execute code and valide differents between the codes. Change the order variable for example.










