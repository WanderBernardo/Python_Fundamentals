# Working with List

Lists in Python can store any type of object sequentially. We can create lists using the list constructor, the range function, or by placing comma-separated values ​​inside square brackets. Lists are mutable objects, so we can change their values ​​after creation.

### Create List

List are create using brackets "[]". It can contain: number, text, mix. Examples:

![image](https://github.com/user-attachments/assets/6c104bdb-93b1-4451-bdbd-1ffd21032a60)

```
frutas = ["laranja", "maca", "uva"]
frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
```

### Directly Accessing the List

The list is a sequence, so we can access its data using indexes. We count the index of a given sequence starting from zero.

![image](https://github.com/user-attachments/assets/1d60a340-806c-429f-9634-431972dd4cd9)

![image](https://github.com/user-attachments/assets/25a50079-4804-4bfc-88f4-7f803b3416da)

```
frutas = ["apple", "orange", "pear", "grape"]

frutas[0]  # apple
frutas[2]  # pear

print (frutas[0])
print ()frutas[2]
```

### Negative Indexes

Sequences support negative indexing. Counting starts at -1. So, it count start of the right to left. 

![image](https://github.com/user-attachments/assets/a7cc74f1-216c-4b92-91d0-b66b3cb85f1e)

```
frutas = ["apple", "orange", "pear", "grape"]

frutas[-1]  # grape
frutas[-3]  # orange

print(frutas[-1])
print(frutas[-3])
```

### Nested List

Lists can store all types of Python objects, so we can have lists that store other lists. With this we can create two-dimensional structures (tables), and access them by informing the row and column indices.

![image](https://github.com/user-attachments/assets/7826a393-cc35-416f-9847-bca55feec941)

We count the index of a given sequence starting from zero:

![image](https://github.com/user-attachments/assets/e1ba1351-cf71-42b3-b131-76540be0db54)

```
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0]  # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1]  # 2
matriz[-1][-1]  # "c"

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
```

### Slicing List

In addition to accessing elements directly, we can extract a set of values ​​from a sequence. To do this, simply pass the initial and/or final index to access the set. We can also specify how many positions the cursor should "jump" to when accessing it.

![image](https://github.com/user-attachments/assets/80ceadbd-607a-4fff-956e-a6104af2e128)

```
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]  # ["t", "h", "o", "n"]
lista[:2]  # ["p", "y"]
lista[1:3]  # ["y", "t"]
lista[0:3:2]  # ["p", "t"]
lista[::]  # ["p", "y", "t", "h", "o", "n"]
lista[::-1]  # ["n", "o", "h", "t", "y", "p"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])
```
