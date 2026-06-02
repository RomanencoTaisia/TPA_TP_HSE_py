class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return (self.name == other.name) and (self.unit == other.unit)


"""flour= Ingredient("MUKA",500,"kg")
apple=Ingredient("YABLOKO",500,"kg")
flour1= Ingredient("MUKA",500,"kg")
print(flour)
print(repr(flour1))
print(flour1.__eq__(flour))"""


class Recipe:
    def __init__(self, title):
        self.title = title
        self.ingredients = []

    def add_ingredient(self, ingredient: Ingredient):
        for ing in self.ingredients:
            if ing == ingredient:
                ing.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int, float)) and (ratio > 0):
            return True
        return False

    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            raise ValueError("Умножать можно только на что-то положительное")
        recipe = Recipe(self.title)
        for ing in self.ingredients:
            scolko_ingredient = Ingredient(
                ing.name, ing.quantity*ratio, ing.unit)
            recipe.add_ingredient(scolko_ingredient)
        return recipe

    def __len__(self):
        return len(self.ingredients)


    def __str__(self):
        outputi= f"Блюдо называется{self.title}.\n"
        outputi+="Ингредиенты- \n"
        for i in range ( len(self.ingredients)):
            ing=self.ingredients[i]
            outputi+=f"{i+1}){ing}\n"
            
        return outputi    

"""4commit"""

    
    
    