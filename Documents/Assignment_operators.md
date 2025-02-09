## Assignment Operators

Sure! Assignment operators are used to assign values to variables in Python. Here's a summary table of the common assignment operators:

Assignment Operators, make a simple arithmetic calculation with the value of the variable by adding the result to this variable.

| Operator | Description | Example  | Explication                                           |
|----------|-------------|----------|-------------------------------------------------------|
| `=`      | Assign      | `a = 5`  | Assigns the value 5 to the variable `a`               |
| `+=`     | Add and assign | `a += 5` | Adds 5 to the value of `a` and assigns the result to `a` |
| `-=`     | Subtract and assign | `a -= 5` | Subtracts 5 from the value of `a` and assigns the result to `a` |
| `*=`     | Multiply and assign | `a *= 5` | Multiplies the value of `a` by 5 and assigns the result to `a` |
| `/=`     | Divide and assign | `a /= 5` | Divides the value of `a` by 5 and assigns the result to `a` |
| `%=`     | Modulus and assign | `a %= 5` | Takes the modulus of `a` by 5 and assigns the result to `a` |
| `**=`    | Exponent and assign | `a **= 2` | Raises the value of `a` to the power of 2 and assigns the result to `a` |
| `//=`    | Floor divide and assign | `a //= 3` | Floor divides the value of `a` by 3 and assigns the result to `a` |

```
a = 10

a += 5   # Equivalent to a = a + 5
print(a) # 15

a -= 3   # Equivalent to a = a - 3
print(a) # 12

a *= 2   # Equivalent to a = a * 2
print(a) # 24

a /= 4   # Equivalent to a = a / 4
print(a) # 6.0

a %= 3   # Equivalent to a = a % 3
print(a) # 0.0

a **= 2  # Equivalent to a = a ** 2
print(a) # 0.0

a //= 2  # Equivalent to a = a // 2
print(a) # 0.0
```

**Details Example:**

Imagine You add R$ 10 in the account bank and your account there was R$ 20 then, total actual: R$ 30:

| Step | Description                     | Code                                |
|------|---------------------------------|-------------------------------------|
| 1    | Initial value of your account: R$ 20 | `Account = 20`                    |
| 2    | Add R$ 10 to your account       | `Account += 10`                     |
| 3    | New value of the account will be R$ 30 | `print(Account)`                 |
