# Local and Global Scope

Basically is declarate variable inside function to "Local Scope" and outside of the function to "Global Scope".

### 1 - Local Scope

![image](https://github.com/user-attachments/assets/3dc83e6e-826e-46a5-bfb7-b4e576647094)

```
def wage_bonus(bonus):
    wage = 2000
    wage +=bonus

    return wage

wage_with_bonus = wage_bonus(500)
print(wage_with_bonus)
```


### 2 - Global Scope

In this case there is reserved word "global". It's necessary to use inside function.

![image](https://github.com/user-attachments/assets/66e361fd-f940-4a5d-9b44-4a5e5ce17026)

```
wage = 2000

def wage_bonus(bonus):
    global wage
    wage +=bonus

    return wage

wage_with_bonus = wage_bonus(500)
print(wage_with_bonus)
```
