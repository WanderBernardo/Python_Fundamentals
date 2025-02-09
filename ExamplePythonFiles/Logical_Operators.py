a = True
b = False

# Logical AND
print(a and b)  # False, because both statements are not True

# Logical OR
print(a or b)   # True, because at least one statement is True

# Logical NOT
print(not a)    # False, because a is True
print(not b)    # True, because b is False




# Logical AND
a = 2
b = 3
if a > 1 and b < 5:
    print("Condition met")  # This will print because both conditions are True

# Logical OR
a = 12
b = 3
if a > 10 or b < 5:
    print("At least one condition met")  # This will print because at least one condition is True

# Logical NOT
a = 8
if not a > 10:
    print("a is not greater than 10")  # This will print because a is not greater than 10