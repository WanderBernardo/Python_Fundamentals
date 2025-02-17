# Manipulating Strings - Part 01

String is value declarated inside of Quotation marks ("").

### Using Upper, Lower and title

- **Upper:** Becomes string all in Uppercase. Example: PyTHon - Outcome: PYTHON
- **Lower:** Becomes string all in Lowercase. Example: PyTHon - Outcome: python
- **Title:** Becomes string all in title. Example: PyTHon - Outcome: Python

Screen

```
curso = "pYtHon"

print(curso.upper())
print(curso.lower())
print(curso.title())
```

### Eliminating white space

- **strip:** Remove space gap of the right and left.
- **lstrip:** Remove space gap of the right and left.
- **rstrip:** Remove space gap of the right and left.

In this case, the outcome doesn't will be see because space is invisible in the code.

Screen

```
curso = "   Python "

print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())
```

### Separate and centralize

- **center:** It centers the text within the desirable character. 
- **join:** Separate each character conform necessary.

Screen

```
curso = "Python"

print(curso.center(10, "#"))
print(".".join(curso))
```
