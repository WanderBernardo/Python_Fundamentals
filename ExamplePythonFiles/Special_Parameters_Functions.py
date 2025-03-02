# 1 - Positional Only
def save_car(brand, model, /, year, license_plate):
    # save car in the database
    print(f"Car insert with sucess! {brand}/{model}/{year}/{license_plate}")

save_car("Fiat","Palio",year=1999,license_plate="ABC-1234")


# 2 - Named Only (Keyword Olny)
def save_car(brand, * ,model,year, license_plate):
    # save car in the database
    print(f"Car insert with sucess! {brand}/{model}/{year}/{license_plate}")

save_car("Fiat",model="Palio",year=1999,license_plate="ABC-1234")


# 3 - Positional with Named Only (Keyword Olny) together
def save_car(brand, / ,model, * ,year, license_plate):    # save car in the database
    print(f"Car insert with sucess! {brand}/{model}/{year}/{license_plate}")

save_car("Fiat",model="Palio",year=1999,license_plate="ABC-1234")
save_car("Fiat","Palio",year=1999,license_plate="ABC-1234")