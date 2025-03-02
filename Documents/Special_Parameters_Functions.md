# Functions: Special Parameters

In previous items, you saw about "Functions" and saw that it's possible incluide arguments for named, positional and positional and named. But it's possibly also add mandatory format. Let's see!!

### 1 - Positional Only

In this case, use "/" and all before "/", mandatory to be positional

![image](https://github.com/user-attachments/assets/4a8ad70d-72a8-40f9-ab99-16fec11ba77e)

Exeample:

```
def save_car(brand, model, /, year, license_plate):
    # save car in the database
    print(f"Car insert with sucess! {brand}/{model}/{year}/{license_plate}")

save_car("Fiat","Palio",year=1999,license_plate="ABC-1234")
```

### 2 - Named Only (Keyword Olny)

In this case, use " * " and all after " * ", mandatory to be named.

![image](https://github.com/user-attachments/assets/18f36bd0-5a8c-49b6-8970-d1d9098eabd0)

Exeample:

```
def save_car(brand, * ,model,year, license_plate):
    # save car in the database
    print(f"Car insert with sucess! {brand}/{model}/{year}/{license_plate}")

save_car("Fiat",model="Palio",year=1999,license_plate="ABC-1234")
```

### 3 - Positional with Named Only (Keyword Olny) together

In this case, use " / " all before and " * " all after.

![image](https://github.com/user-attachments/assets/a1b842f6-f50f-49d5-be7f-524695e947e8)

Exeample:

```
def save_car(brand, / ,model, * ,year, license_plate):
    # save car in the database
    print(f"Car insert with sucess! {brand}/{model}/{year}/{license_plate}")

save_car("Fiat",model="Palio",year=1999,license_plate="ABC-1234")
save_car("Fiat","Palio",year=1999,license_plate="ABC-1234")
```
