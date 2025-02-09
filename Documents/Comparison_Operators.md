### Document:

- https://docs.python.org/pt-br/3.13/library/operator.html

## Comparison Operators

Comparison operators are used in programming to compare two values or variables.

| Operator | Description               | Example | Result | Explication                           |
|----------|---------------------------|---------|--------|---------------------------------------|
| `==`     | Equal to                  | `5 == 5`| `True` | Equality: Checks if the values are equal |
| `!=`     | Not equal to              | `5 != 2`| `True` | Inequality: Checks if the values are not equal |
| `>`      | Greater than              | `5 > 3` | `True` | Greater than: Checks if the left value is greater than the right value |
| `<`      | Less than                 | `5 < 10`| `True` | Less than: Checks if the left value is less than the right value |
| `>=`     | Greater than or equal to  | `5 >= 5`| `True` | Greater than or equal to: Checks if the left value is greater than or equal to the right value |
| `<=`     | Less than or equal to     | `5 <= 8`| `True` | Less than or equal to: Checks if the left value is less than or equal to the right value |

Here's a quick example of using these operators:
```
a = 10
b = 5

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False
```

## Examples using function:

**Conditional Statements:** Used in if, elif, and else statements to execute code blocks based on certain conditions:
```
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

**Loops:** Used in while loops to continue looping as long as a condition is true.
```
count = 0
while count < 5:
    print(count)
    count += 1
```

**List Comprehensions:** Used to filter elements in a list.
```
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # [2, 4, 6]
```

**Sorting and Searching:** Used to compare elements while sorting or searching in data structures.
```
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)  # Uses comparison operators internally
print(sorted_numbers)  # [1, 2, 5, 5, 6, 9]
```

**Assertions:** Used to test conditions that must be true in your code.
```
assert 2 + 2 == 4, "Math error!"
print("Assertion passed")  # This will be printed if the assertion is true
```

### Return principal Menu

https://github.com/WanderBernardo/Python_Fundamentals
