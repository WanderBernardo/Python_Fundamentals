# Indentation and Blocks

It is necessary to use indentation for Python to understand the sequence of execution and block limits

Good practices:

- Indent code using four spaces per level. You can also use a single tab, but spaces are preferred for consistency.

- All the code that belongs to the same block must be indented equally.


Example:

Don't worried about understand the fuctions. in this moment look Indentation and Blocks.

![image](https://github.com/user-attachments/assets/dfd839e6-31a9-4651-9e27-927564258ee9)

![image](https://github.com/user-attachments/assets/ccfe1efd-457d-44cc-8509-a2abf0c703af)

![image](https://github.com/user-attachments/assets/65ef4b66-fde7-443f-b16f-570e079c026b)



```
# Function Definitions:
def my_function():
    # This block belongs to my_function
    print("Hello, World!")

# Loops:
for i in range(5):
    # This block belongs to the for loop
    print(i)

# Conditional Statements 01:
if True:
    # This block belongs to the if statement
    print("This is true!")
else:
    # This block belongs to the else statement
    print("This is false!")

# Nested Blocks:
for i in range(3):
    if i % 2 == 0:
        # Nested block inside the for loop and if statement
        print(f"{i} is even")
    else:
        # Nested block inside the for loop and else statement
        print(f"{i} is odd")

# Conditional Statements 02:
if True:
    # This block belongs to the if statement
    print("This is true!")
elif False:
    # This block belongs to the elif statement
    print("This is elif true!")
else:
    # This block belongs to the else statement
    print("This is false!")

```
