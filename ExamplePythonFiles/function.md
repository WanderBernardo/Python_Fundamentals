# Functions

It's a block of code identified by a name and can receive a list of parameters, these parameters may or may not have default values. Using functions makes code more readable and makes it possible to reuse code. Programming based on functions is the same as saying that we are programming in a structured way.

![image](https://github.com/user-attachments/assets/4d9330a2-54aa-44d0-863b-5aad2ff8a156)

### Build in three way:

**1 - Without Arguments:**

![image](https://github.com/user-attachments/assets/dc6cb8fb-88f8-4081-8163-09ed467797ff)

```
def show_mensage1():
    print("Hello, World!!")
```

**2 - With Arguments:**

In this case, when running the code is mandatory include arguments it. And if forget, code show error.

![image](https://github.com/user-attachments/assets/ad598ddd-63a4-4924-8731-38b6b13a1a6d)

```
def show_mensage2(name):
    print(f"Hello {name}, World!!")
```

**3 - With Arguments and return standard:**

In this case, if you forget include armments when running the code, It will be used standard return.  

![image](https://github.com/user-attachments/assets/18de2fae-f076-410d-a0c5-7295ef2377d4)

```
def show_mensage3(name="Anonymous"):
    print(f"Hello {name}, World!!")
```

### How use the function:

Very simple, type name of  function and include arguments case to be necessary.

![image](https://github.com/user-attachments/assets/e7380f05-4bda-43b8-a834-b178dc6c4e5c)

```
show_mensage1()  # Case 01
show_mensage2(name="Julia")  # Case 02
show_mensage3()  # Case 03
show_mensage3(name="Guilherme")  # Case 03
```

### Return more one value

To some programming language the functions only return one result. In Python is possible return more one.

![image](https://github.com/user-attachments/assets/9d9022a6-98b4-4260-9d5b-48146b189181)

```
def calculate_total(numbers):
    return sum(numbers)

def return_predecessor_successor(number):
    predecessor = number - 1
    successor = number + 1

    return predecessor, successor


print(calculate_total([10, 20, 30])) # result 50
print(return_predecessor_successor(10)) # result (9, 11)
```

**Case, it doesn't include "return" in the end of the intruction, for standard the return wil be "None". but, it can use "return None""**

I executed the function without providing the required arguments.

![image](https://github.com/user-attachments/assets/59281af3-5356-47d1-b9fb-ccf208d33250)

```
def none1():
    print("Hello, World!!")

# OR

def none2():
    print("Hello, World!!")

    return None

print(none1()) # Result None
print(none2()) # Result None
```







