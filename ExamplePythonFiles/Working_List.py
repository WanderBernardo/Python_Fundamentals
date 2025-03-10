# frutas = ["laranja", "maca", "uva"]
# frutas = []
# letras = list("python")
# numeros = list(range(10))
# carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]



# Directly Accessing the List

frutas = ["apple", "orange", "pear", "grape"]

frutas[0]  # apple
frutas[2]  # pear

print(frutas[0])  # apple
print(frutas[2])  # pear


# Negative Indexes

frutas = ["apple", "orange", "pear", "grape"]

frutas[-1]  # grape
frutas[-3]  # orange

print(frutas[-1])  # grape
print(frutas[-3])  # orange

# Nested List

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0]  # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1]  # 2
matriz[-1][-1]  # "c"

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

# Slicing List

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
