### Conditional Structures: IF, IF ELSE and IF ELIF ELSE

Conditional Structures are used when is need to make a decision and know how many decisions there are.

## IF

- Simple decision 
- One alternative

If the condition is True, it executes a block of code.

![image](https://github.com/user-attachments/assets/9d2cc4a7-b105-4f0b-a931-c7db8ab1c662)

Look, it was used Comparison Operators.

```
num = 10
if num > 5:
    print("Number is greater than 5")
```


## IF ELSE

- Two only alternative

It's used to execute one block of code if the condition is True and another block if the condition is False.


Look, the ":" sign also goes in "else". Do part of the structure function.

```
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```


## IF ELIF ELSE

- Three alternative or more

It's used for multiple conditions where you have several possibilities to consider. Example: traffic light.

```
light_color = "green"  # This can be "green", "yellow", or "red"

if light_color == "green":
    print("Go")
elif light_color == "yellow":
    print("Prepare to Stop")
else:
    print("Stop")
```


