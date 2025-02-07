
### Document:

- https://docs.python.org/3/library/stdtypes.html


### Python offers several built-in data types, each designed to store specific types of data:

| **Category**      | **Data Type** | **Description**                                | **Example**                       |
|-------------------|---------------|------------------------------------------------|-----------------------------------|
| Numeric Types     | `int`         | Whole numbers                                  | `5`, `100`                        |
|                   | `float`       | Numbers with decimals                          | `3.14`, `2.0`                     |
|                   | `complex`     | Complex numbers                                | `1+2j`                            |
| Sequence Types    | `str`         | Sequence of characters                         | `"hello"`, `'Python'`             |
|                   | `list`        | Ordered collection of items                    | `[1, 2, 3]`, `["apple", "banana", "cherry"]` |
|                   | `tuple`       | Ordered and immutable collection of items      | `(1, 2, 3)`, `("apple", "banana", "cherry")` |
| Mapping Types     | `dict`        | Collection of key-value pairs                  | `{"name": "Alice", "age": 25}`    |
| Set Types         | `set`         | Unordered collection of unique items           | `{1, 2, 3}`, `{"apple", "banana", "cherry"}` |
|                   | `frozenset`   | Immutable set                                  | `frozenset({1, 2, 3})`            |
| Boolean Type      | `bool`        | Represents `True` or `False` values            | `True`, `False`                   |
| Binary Types      | `bytes`       | Immutable sequences of bytes                   | `b'hello'`                        |
|                   | `bytearray`   | Mutable sequences of bytes                     | `bytearray(b'hello')`             |
|                   | `memoryview`  | Memory view object exposing buffer interface   | `memoryview(b'hello')`            |

### Example practice via VSCode:

```
# Integer
int_example = 10
print("Integer:", int_example)

# Float
float_example = 3.14
print("Float:", float_example)

# String
str_example = "Hello, Python!"
print("String:", str_example)

# List
list_example = [1, 2, 3, "apple", "banana", "cherry"]
print("List:", list_example)

# Tuple
tuple_example = (1, 2, 3, "apple", "banana", "cherry")
print("Tuple:", tuple_example)

# Dictionary
dict_example = {"name": "Alice", "age": 25}
print("Dictionary:", dict_example)

# Set
set_example = {1, 2, 3, "apple", "banana", "cherry"}
print("Set:", set_example)

# Boolean
bool_example = True
print("Boolean:", bool_example)

# Complex
complex_example = 1 + 2j
print("Complex number:", complex_example)

# Bytes
bytes_example = b"Hello"
print("Bytes:", bytes_example)

# Bytearray
bytearray_example = bytearray(b"Hello")
print("Bytearray:", bytearray_example)

# Memoryview
memoryview_example = memoryview(b"Hello")
print("Memoryview:", memoryview_example)

```

### Pay Attetion

When you will use some data type, the structure change.

Example:

01 - list_example = [1, 2, 3, "apple", "banana", "cherry"]
02 - tuple_example = (1, 2, 3, "apple", "banana", "cherry")

What's different?

List type: use "[]" and tuple use "()".
