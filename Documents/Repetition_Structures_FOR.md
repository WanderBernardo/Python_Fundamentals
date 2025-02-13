# Repetition Structures: FOR

It's used to execute a block of code multiple times and know how many times will be done. These structures are commonly referred to as loops.

**Example without "FOR":**

Get a number of the keyboard and exhibit the two after number.

![image](https://github.com/user-attachments/assets/351233ab-2746-4889-aafe-f833050fa915)

Case, you want of the 10 after result, need repet 10 times "a += 1, print(a)".

```
a = int(input("Inform an integer number: "))

a += 1
print(a)

a += 1
print(a)
```


**Example with "FOR":**

The same example above:

![image](https://github.com/user-attachments/assets/a2fc8ee4-0f21-40c6-a473-ac1e574d768a)

The range(2) creates a sequence of numbers [0, 1], meaning the loop will run twice.

The _ is a common convention in Python to indicate that the loop variable is not going to be used.

This way, the loop handles the repetition of incrementing and printing the value of a. If you want to repeat this action more times, you can change the number inside range(). For example, range(5) would run the loop five times.

```
a = int(input("Inform an integer number: "))

for _ in range(2):
    a += 1
    print(a)
```

## The outcome is the same. What's different than?

Simple! Effort the create code.

Now, you need result the next 20 number. Try to make with both code (with and Without FOR). 


### Other point: each class is used concepts before.
