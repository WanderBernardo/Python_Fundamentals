# Local and Global Scope

Basically is declarate variable inside function to "Local Scope" and outside of the function to "Global Scope".

### 1 - Local Scope

```
def wage_bonus(bonus)
    wage = 2000
    wage +=bonus

    return wage

wage_with_bonus = wage_bonus(500)
print(wage_with_bonus)
```


### 2 - Global Scope

In this case there is reserved word "global". It's necessary to use inside function.

```
wage = 2000

def wage_bonus(bonus)
    global wage
    wage +=bonus

    return wage

wage_with_bonus = wage_bonus(500)
print(wage_with_bonus)
```
