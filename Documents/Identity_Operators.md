
## Identity Operators: "IS" and "IS NOT"

Are used to compare the memory locations of two objects.

- "is": Returns True if both variables point to the same object.

- "is not": Returns True if both variables do not point to the same object. (Invert the result)


**Example:** You have two books, but one is a copy, not original. So, a friend asked you to borrow it and you don't want to lend the original. How will you know the difference between the two, to lend the copy?

Soluction: Identity Operators:

```
# Creating two variables with the same value
Book Original = [1, 2, 3]
Book Copy = [1, 2, 3]
Friend = Book Copy

# Using 'is' operator
print(Book Original is Book Copy)  # Outputs: False (Book Original and Book Copy are different local in bookshelf)
print(Book Copy is Friend)  # Outputs: True (Book Copy and Friend is pointing the same local in bookshelf)

# Using 'is not' operator
print(Book Original is not Book Copy)  # Outputs: True (Book Original and Book Copy are different local)
print(Book Original is not Friend)  # Outputs: False (Book Original and Friend point to the same local)
```


