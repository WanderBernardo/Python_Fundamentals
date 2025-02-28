# Named Functions, Named Arguments or User-Defined Functions

It's basely you define these functions using the "def" keyword, followed by the function name, parentheses (which may include parameters), and a colon. The code block within the function is indented. Let's see examples:

### There are 3 ways to use Named Functions:

```
def save_car(brand, model, year, license_plate)
    # save car in the database
    print(f' Car insert with sucess! {brand}/{model}/{year}/{license_plate})
```
#### 1 - Calling the function including the values ​​directly:

In this case, pay attetion because the order of the arguments need to be of the same sequence.

```
save_car("Fiat","Palio",1999,"ABC-1234")
```

Case, It's not include the same sequence. Python gonna accept, without error. Example with error:

```
save_car("Palio","Fiat",1999,"ABC-1234")
```

Compare with case above.

#### 2 - Calling the function including the set: key and values:

- In this case, there is benefit. Because if change order of the arguments Python understand and identifies order correct and aplly correctly. in this example: save in the database.

- Other point is case change name of the argument python doesn't find need change both locate: in function declaration and call.

    ```
    save_car(brand="Fiat",model="Palio",year=1999,license_plate="ABC-1234")
    save_car(year=1999,brand="Fiat",license_plate="ABC-1234",modelXXXXX="Palio")
    ```

#### 3 - Calling the function including inside "dictionary".

- In this case, there is benefit. Because if change order of the arguments Python understand and identifies order correct and aplly correctly. in this example: save in the database.

- Other point is case change name of the argument python doesn't find need change both locate: in function declaration and call.

    ```
    save_car(**{year=1999,brand="Fiat",license_plate="ABC-1234",model="Palio"})
    ```
