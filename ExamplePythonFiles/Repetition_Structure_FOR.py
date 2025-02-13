
# Use interative mode with block.

# Without FOR

a = int(input("Inform an integer number: "))

a += 1
print(a)

a += 1
print(a)


# With FOR

a = int(input("Inform an integer number: "))

for _ in range(2):
    a += 1
    print(a)
