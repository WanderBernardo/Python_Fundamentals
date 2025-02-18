# Repetition Structures: WHILE

It's used to repet a block code several times. Ideal when not know how many times block code need excute.

Example: Print when number least that 5. In this case, the user can put any number. So, It was used While. we don't know when number it will be put.

![image](https://github.com/user-attachments/assets/2475ab7a-4e96-4293-b0af-d3297897cb54)

```
count = 1
while count <= 5:
    print(f'Number: {count}')
    count += 1
```

# WHILE ELSE

Use ELSE in the end "WHILE" when need include a condition, case outcome not enter "WHILE". Example:

This else block provides a way to perform an action after the loop completes its normal iteration.

![image](https://github.com/user-attachments/assets/9c333ea2-6f30-4536-a298-91df348214b2)

```
count = 1
while count <= 5:
    print(f'Number: {count}')
    count += 1
else:
    print('The loop has finished.')
```
