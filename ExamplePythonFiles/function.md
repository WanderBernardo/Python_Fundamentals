# Functions

It's a block of code identified by a name and can receive a list of parameters, these parameters may or may not have default values. Using functions makes code more readable and makes it possible to reuse code. Programming based on functions is the same as saying that we are programming in a structured way.

![image](https://github.com/user-attachments/assets/3091d4f8-c974-4688-8a2f-9856c2b7574d)


### Build in three way:

**1 - Without Arguments:**

```
def show_mensage1()
    print(Hello, World!!)
```

**2 - With Arguments:**

In this case, when running the code is mandatory include arguments it. And if forget, code show error.

```
def show_mensage2name)
    print(f"Hello {name}, World!!)
```

**3 - With Arguments and return standard:**

In this case, if you forget include armments when running the code, It will be used standard return.  

```
def show_mensage3(name="Anonymous")
    print(f"Hello {name}, World!!)
```

### How use the function:

Very simple, type name of  function and include arguments case to be necessary.

```
show_mensage1()  # Case 01
show_mensage2(name="Julia")  # Case 02
show_mensage3()  # Case 03
show_mensage3(name="Guilherme")  # Case 03
```

### Return more one value

To some programming language the functions only return one result. In Python is possible return more one.

```
def calculate_total(numbers)
    return sum(numbers)

def return_predecessor_successor(number)
    predecessor = number - 1
    successor = number + 1

    return predecessor, successor


calculate_total([10, 20, 30]) # result 50
return_predecessor_successor(10) # result (9, 11)
```

**Case, it doesn't include "return" in the end of the intruction, for standard the return wil be "None". but, it can use "return None""**

I executed the function without providing the required arguments.

```
def none1()
    print(Hello, World!!)

# OR

def none2()
    print(Hello, World!!)

    return None

print(none1()) # Result None
print(none2()) # Result None
```







