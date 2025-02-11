
# Use interative mode

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        print(f"Created recipe: {self.name} with ingredients: {', '.join(self.ingredients)}")

    def cook(self):
        return f"Cooking {self.name} with {', '.join(self.ingredients)}"

# Practice:
# Create a Recipe class with attributes name and ingredients, and a method cook. 



# Creating an instance of Recipe
carbonara = Recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "bacon", "parmesan"])
print(carbonara.cook())  # Outputs: Cooking Spaghetti Carbonara with spaghetti, eggs, bacon, parmesan

# Practice:
# Create an object of the Recipe class, and call its cook method.



# Accessing attributes
print(carbonara.name)        # Outputs: Spaghetti Carbonara
print(carbonara.ingredients) # Outputs: ['spaghetti', 'eggs', 'bacon', 'parmesan']

# Practice:
# Access the name and ingredients attributes of the carbonara object.



# Adding a method to the Recipe class
class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        print(f"Created recipe: {self.name} with ingredients: {', '.join(self.ingredients)}")

    def cook(self):
        return f"Cooking {self.name} with {', '.join(self.ingredients)}"

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"Added ingredient: {ingredient}")
        return self.ingredients

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)
        print(f"Removed ingredient: {ingredient}")
        return self.ingredients

# Creating an instance and using methods
carbonara = Recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "bacon", "parmesan"])
print(carbonara.cook())  # Outputs: Cooking Spaghetti Carbonara with spaghetti, eggs, bacon, parmesan
carbonara.add_ingredient("black pepper")
print(carbonara.ingredients) # Outputs: ['spaghetti', 'eggs', 'bacon', 'parmesan', 'black pepper']
carbonara.remove_ingredient("bacon")
print(carbonara.ingredients) # Outputs: ['spaghetti', 'eggs', 'parmesan', 'black pepper']

# Practice:
# Add methods add_ingredient and remove_ingredient to the Recipe class, 
# and use them to modify the ingredients of the carbonara object.



# Example full:

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        print(f"Created recipe: {self.name} with ingredients: {', '.join(self.ingredients)}")

    def cook(self):
        return f"Cooking {self.name} with {', '.join(self.ingredients)}"

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"Added ingredient: {ingredient}")
        return self.ingredients

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)
        print(f"Removed ingredient: {ingredient}")
        return self.ingredients

# Creating an instance and using methods
carbonara = Recipe("Spaghetti Carbonara", ["spaghetti", "eggs", "bacon", "parmesan"])
print(carbonara.cook())  # Outputs: Cooking Spaghetti Carbonara with spaghetti, eggs, bacon, parmesan
carbonara.add_ingredient("black pepper")
print(carbonara.cook())  # Outputs: Cooking Spaghetti Carbonara with spaghetti, eggs, bacon, parmesan, black pepper
carbonara.remove_ingredient("bacon")
print(carbonara.cook())  # Outputs: Cooking Spaghetti Carbonara with spaghetti, eggs, parmesan, black pepper
