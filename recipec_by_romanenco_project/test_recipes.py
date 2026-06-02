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



    
           
         
      
        