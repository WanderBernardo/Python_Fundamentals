
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



# FOR ELSE

# Checking username availability using for-else

registered_users = ['alice', 'bob', 'carol', 'dave']
new_user = 'eve'

for user in registered_users:
    if user == new_user:
        print(f'The username "{new_user}" is already taken. Please choose another one.')
        break
else:
    print(f'The username "{new_user}" is available!')
