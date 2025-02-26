def show_mensage1():
    print("Hello, World!!")


def show_mensage2(name):
    print(f"Hello {name}, World!!")


def show_mensage3(name="Anonymous"):
    print(f"Hello {name}, World!!")



show_mensage1()  # Case 01
show_mensage2(name="Julia")  # Case 02
show_mensage3()  # Case 03
show_mensage3(name="Guilherme")  # Case 03



def calculate_total(numbers):
    return sum(numbers)

def return_predecessor_successor(number):
    predecessor = number - 1
    successor = number + 1

    return predecessor, successor



print(calculate_total([10, 20, 30])) # result 50
print(return_predecessor_successor(10)) # result (9, 11)


def none1():
    print("Hello, World!!")

# OR

def none2():
    print("Hello, World!!")

    return None

print(none1()) # Result None
print(none2()) # Result None