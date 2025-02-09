## Logical Operators

Are used to evaluate expressions and combine multiple conditions.

| Operator | Description | Example  | Explication |
|----------|-------------|----------|-------------|
| `and`    | Logical AND | `True and False` | Returns `True` if both statements are `True`, otherwise returns `False` |
| `or`     | Logical OR  | `True or False`  | Returns `True` if at least one statement is `True`, otherwise returns `False` |
| `not`    | Logical NOT | `not True`       | Returns `False` if the statement is `True`, and `True` if the statement is `False` |

```
a = True
b = False

# Logical AND
print(a and b)  # False, because both statements are not True

# Logical OR
print(a or b)   # True, because at least one statement is True

# Logical NOT
print(not a)    # False, because a is True
print(not b)    # True, because b is False
```

### Example Practice
```
# Logical AND
a = 2
b = 3
if a > 1 and b < 5:
    print("Condition met")  # This will print because both conditions are True

# Logical OR
a = 12
b = 3
if a > 10 or b < 5:
    print("At least one condition met")  # This will print because at least one condition is True

# Logical NOT
a = 8
if not a > 10:
    print("a is not greater than 10")  # This will print because a is not greater than 10
```

### Return principal Menu

https://github.com/WanderBernardo/Python_Fundamentals
