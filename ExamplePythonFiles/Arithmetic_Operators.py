# Arithmetic Operators

Number01 = 5
number02 = 3

Result = Number01 + number02
print(Result)

Result = Number01 - number02
print(Result)

Result = Number01 * number02
print(Result)

Result = Number01 / number02
print(Result)

Result = Number01 // number02
print(Result)

Result = Number01 % number02
print(Result)

Result = Number01 ** number02
print(Result)


# Precedence Arithmetic Operators

# Order - Without paratheses
#01. Exponentiation (**)
# 02. Multiplication (*), Division (/), Floor Division (//), Modulus (%)
# 03. Addition (+), Subtraction (-)

result = 5 + 3 * 2 ** 2 / 4 - 1
print(result)


# Order - With paratheses

result_with_parentheses = ((5 + 3) * 2 ** 2) / (4 - 1)
print(result_with_parentheses)

#Parentheses: (5 + 3) results in 8
#Exponentiation: 2 ** 2 results in 4
#Multiplication: 8 * 4 results in 32
#Parentheses: (4 - 1) results in 3


# No problem!!! Remember the numerical expression from mathematics!