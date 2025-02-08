
### Document:

- https://docs.python.org/pt-br/3.13/library/operator.html


## Arithmetic Operators

Are used to perform basic mathematical operations.

| Operator      | Description                           | Example | Practical Example |
|---------------|---------------------------------------|--------------------|----------------------------------------------|
| `+` (Addition) | Adds two numbers                      | `5 + 3`            | `total_items = apples + oranges; print(total_items)` |
| `-` (Subtraction) | Subtracts the second number from the first | `5 - 3`            | `remaining_balance = total - spent; print(remaining_balance)` |
| `*` (Multiplication) | Multiplies two numbers                | `5 * 3`            | `total_cost = price_per_item * quantity; print(total_cost)` |
| `/` (Division)      | Divides the first number by the second (always returns a float) |`5 / 3`             | `average_score = total_points / number_of_games; print(average_score)` |
| `//` (Floor Division) | Divides the first number by the second and rounds down to the nearest whole number | `5 // 3`           | `full_boxes = total_items // items_per_box; print(full_boxes)` |
| `%` (Modulus)       | Returns the remainder of the division of the first number by the second | `5 % 3`            | `remaining_items = total_items % items_per_box; print(remaining_items)` |
| `**` (Exponentiation) | Raises the first number to the power of the second | `5 ** 3`           | `area = side_length ** 2; print(area)` |


## Precedence Arithmetic Operators

The precedence of arithmetic operators determines the order in which operations are performed in an expression. Operators with higher precedence are executed before those with lower precedence.

1. Exponentiation (**)

2. Multiplication (*), Division (/), Floor Division (//), Modulus (%)

3. Addition (+), Subtraction (-)


Example:
```
result = 5 + 3 * 2 ** 2 / 4 - 1

print(result)
``` 

Let's see with more details:

 - Exponentiation (2 ** 2 results in 4)

 - Multiplication (3 * 4 results in 12)

 - Division (12 / 4 results in 3.0)

 - Addition (5 + 3.0 results in 8.0)

 - Subtraction (8.0 - 1 results in 7.0)

So, the final result printed is 7.0.

But, when use parentheses. The result change, because the order of execution is different.

```
result_with_parentheses = ((5 + 3) * 2 ** 2) / (4 - 1)

print(result_with_parentheses)
```

 - Parentheses: (5 + 3) results in 8

 - Exponentiation: 2 ** 2 results in 4

 - Multiplication: 8 * 4 results in 32

 - Parentheses: (4 - 1) results in 3

 - Division: 32 / 3 results in 10.666666666666666

So, the final result printed for result_with_parentheses is 10.666666666666666.


### No problem!!! Remember the numerical expression from mathematics!
