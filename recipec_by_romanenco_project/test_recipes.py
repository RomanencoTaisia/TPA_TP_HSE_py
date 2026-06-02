import pytest
from recipec import Ingredient,Recipe,ShoppingList,DietaryRecipe
"""for ingredients"""
def test_creation():
    ingredient = Ingredient("корнецеи", 500, "г")
    assert ingredient.name == "корнецеи"
    assert ingredient.quantity == 500.0
    assert ingredient.unit == "г"

def test_str():
    ingredient = Ingredient("корнецеи", 500, "г")
    assert str(ingredient) == "корнецеи: 500.0 г"

def test_eq_ingr():
    ingredient1 = Ingredient("корнецеи", 500, "г")
    ingredient2 = Ingredient("корнецеи", 200, "г")

    assert ingredient1 == ingredient2
    
def test_eq_ingr2():
    ingredient1 = Ingredient("корнецеи", 500, "г")
    ingredient2 = Ingredient("Сахар", 500, "г")

    assert ingredient1 != ingredient2    
    
def test_eq_ingr3():
    ingredient1 = Ingredient("корнецеи", 500, "г")
    ingredient2 = Ingredient("корнецеи", 500, "кг")

    assert ingredient1 != ingredient2    



"""testi for recipies"""


def test_create():
    recipe = Recipe("Mamaliga")
    assert recipe.title == "Mamaliga"
    assert recipe.ingredients == []

def test_add_ingredient():
    recipe = Recipe("Mamaliga")
    flour = Ingredient("corn flour", 500, "г")
    recipe.add_ingredient(flour)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].name == "corn flour"
    assert recipe.ingredients[0].quantity == 500
    assert recipe.ingredients[0].unit == "г"


def test_add_same_ingredient():
    recipe = Recipe("Льняная каша")

    flour1 = Ingredient("Мука льняная", 50, "г")
    flour2 = Ingredient("Мука льняная", 20, "г")
    recipe.add_ingredient(flour1)
    recipe.add_ingredient(flour2)
    
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].name == "Мука льняная"
    assert recipe.ingredients[0].quantity == 70
    assert recipe.ingredients[0].unit == "г"


def test_scale():
    recipe = Recipe("Яичница по-молдавски")
    recipe.add_ingredient(Ingredient("Яйца",2, "шт"))
    recipe.add_ingredient(Ingredient("Творог", 200, "г"))
    scaled_recipe = recipe.scale(2)

    assert scaled_recipe is not recipe
    assert isinstance(scaled_recipe, Recipe)
    assert recipe.ingredients[0].quantity == 2
    assert recipe.ingredients[1].quantity == 200
    assert scaled_recipe.ingredients[0].quantity == 4
    assert scaled_recipe.ingredients[1].quantity == 400


def test_scale2():
    recipe = Recipe("Орешки с медом")
    recipe.add_ingredient(Ingredient("Орешки", 10, "кг"))
    with pytest.raises(ValueError):
        recipe.scale(0)


def test_scale3():
    recipe = Recipe("Орешки с медом")
    recipe.add_ingredient(Ingredient("Орешки", 10, "кг"))
    with pytest.raises(ValueError):
        recipe.scale(-10)


def test_len():
    recipe = Recipe("Орешки с медом")
    recipe.add_ingredient(Ingredient("Орешки", 500, "г"))
    recipe.add_ingredient(Ingredient("Мед", 20, "г"))
    recipe.add_ingredient(Ingredient("Орешки", 100, "г"))
    
    assert len(recipe) == 2
    
           
         
      
        