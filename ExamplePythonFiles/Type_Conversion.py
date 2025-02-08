
#String to Integer
age_str = "21"
age = int(age_str)
print(age)

# Integer to String
score = 99
score_str = str(score)
print(score_str)

# String to Float
price_str = "19.99"
price = float(price_str)
print(price)

# Float to String
temperature = 36.6
temp_str = str(temperature)
print(temp_str)

# Integer to Float
whole_number = 50
float_number = float(whole_number)
print(float_number)

# List to Tuple
numbers = [4, 5, 6]
num_tuple = tuple(numbers)
print(num_tuple)

# Tuple to List
coords = (7, 8, 9)
coords_list = list(coords)
print(coords_list)

# String to List
word = "python"
letters = list(word)
print(letters)

# List to String
chars = ['c', 'o', 'd', 'e']
word = "".join(chars)
print(word)

# Dictionary to List
person = {'name': 'Alice', 'age': 30}
keys_list = list(person)
print(keys_list)

# List to Dictionary
pairs = [('x', 10), ('y', 20)]
coords_dict = dict(pairs)
print(coords_dict)


# Integer to Float: Carrying out a division of values
10 / 2

# Float to integer: in this case, valeu after decimal point is ignored
preco = 10.30
print = int(preco)

# Integer to integer: Carrying out a division of values with doble slash
10 // 3


# Case with error
preco = "Error"
print(float(preco))