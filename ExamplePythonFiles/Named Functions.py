def save_car(brand, model, year, license_plate):
    # save car in the database
    print(f"Car insert with sucess! {brand}/{model}/{year}/{license_plate}")
          

# Calling the function including the values ​​directly:
save_car("Fiat","Palio",1999,"ABC-1234")
save_car("Palio","Fiat",1999,"ABC-1234")

# Calling the function including the set: key and values:
save_car(brand="Fiat",model="Palio",year=1999,license_plate="ABC-1234")

          
# Calling the function including inside "dictionary".
save_car(**{"brand":"Fiat","model":"Palio","year":1999,"license_plate":"ABC-1234"})
