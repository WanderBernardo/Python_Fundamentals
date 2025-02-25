# Manipulating Strings - Part 01

String is value declarated inside of Quotation marks ("").

### Documents:
- https://docs.python.org/pt-br/3/library/string.html
- https://docs.python.org/pt-br/3/library/stdtypes.html#textseq

### Using Upper, Lower and title

- **Upper:** Becomes string all in Uppercase. Example: PyTHon - Outcome: PYTHON
- **Lower:** Becomes string all in Lowercase. Example: PyTHon - Outcome: python
- **Title:** Becomes string all in title. Example: PyTHon - Outcome: Python

![image](https://github.com/user-attachments/assets/bff32649-151a-4173-bd6c-f61e07212cf0)

```
curso = "pYtHon"

print(curso.upper())
print(curso.lower())
print(curso.title())
```

### Eliminating white space

- **strip:** Remove space gap of the right and left.
- **lstrip:** Remove space gap of the left.
- **rstrip:** Remove space gap of the right.

In this case, the outcome doesn't will be see because space is invisible in the code.

![image](https://github.com/user-attachments/assets/6f0c271f-cca3-4c70-80d2-9fe504b7f020)

```
curso = "   Python "

print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())
```

### Separate and centralize

- **center:** It centers the text within the desirable character. 
- **join:** Separate each character conform necessary.

![image](https://github.com/user-attachments/assets/1d3550fc-9f73-4440-8701-ad647ddfe75f)

```
curso = "Python"

print(curso.center(10, "#"))
print(".".join(curso))
```
