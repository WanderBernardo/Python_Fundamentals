# Creating two variables with the same value
book_original = [1, 2, 3]
book_copy = [1, 2, 3]
friend = book_copy

# Using 'is' operator
print(book_original is book_copy)  # Outputs: False (Book Original and Book Copy are different local in bookshelf)
print(book_copy is friend)  # Outputs: True (Book Copy and Friend is pointing the same local in bookshelf)

# Using 'is not' operator
print(book_original is not book_copy)  # Outputs: True (Book Original and Book Copy are different local)
print(book_copy is not friend)  # Outputs: False (Book Cpoy and Friend point to the same local)