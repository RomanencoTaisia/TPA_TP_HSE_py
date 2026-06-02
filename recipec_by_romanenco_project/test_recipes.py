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
    
           
"""tests for Shopping List"""

def test_add_recipe():
    recipe = Recipe("Орешки со сгущенкой")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Сахар", 100, "г"))
    lst = ShoppingList()
    lst.add_recipe(recipe, 1)
    result = lst.get_list()

    assert len(result) == 2
    assert result[0].name == "Мука"
    assert result[0].quantity == 500
    assert result[0].unit == "г"
    assert result[1].name == "Сахар"
    assert result[1].quantity == 100
    assert result[1].unit == "г"
         
def test_portions():
    recipe = Recipe("Хачапури по аджарски")
    recipe.add_ingredient(Ingredient("Сыр", 300, "г"))
    lst = ShoppingList()

    with pytest.raises(ValueError):
        lst.add_recipe(recipe, -5)

def test_remove_recipe():
    recipe = Recipe("Хачапури по аджарски")
    recipe.add_ingredient(Ingredient("Сыр", 300, "г"))

    recipe2 = Recipe("Хачапури по мергельски")
    recipe2.add_ingredient(Ingredient("Тесто", 400, "г"))

    lst = ShoppingList()
    lst.add_recipe(recipe, 1)
    lst.add_recipe(recipe2, 1)
    
    lst.remove_recipe("Хачапури по мергельски")
    afterall = lst.get_list()

    assert len(afterall) == 1
    assert afterall[0].name == "Сыр"
    assert afterall[0].quantity == 300
    assert afterall[0].unit == "г"
    
def test_remove_recipe_notexist():
    recipe = Recipe("Хачапури по аджарски")
    recipe.add_ingredient(Ingredient("Сыр", 300, "г"))

    recipe2 = Recipe("Хачапури по мергельски")
    recipe2.add_ingredient(Ingredient("Тесто", 400, "г"))

    lst = ShoppingList()
    lst.add_recipe(recipe, 1)
    lst.add_recipe(recipe2, 1)
    
    lst.remove_recipe("Хачапури по имертильски")
    afterall = lst.get_list()

    assert len(afterall) == 2
    assert afterall[0].name == "Сыр"
    assert afterall[0].quantity == 300
    assert afterall[0].unit == "г"
        
def test_get_list_same_ingr():
    recipe = Recipe("Хачапури по аджарски")
    recipe.add_ingredient(Ingredient("Сыр", 300, "г"))

    recipe2 = Recipe("Хачапури по мергельски")
    recipe2.add_ingredient(Ingredient("Сыр", 300, "г"))

    lst = ShoppingList()
    lst.add_recipe(recipe, 1)
    lst.add_recipe(recipe2, 1)

    result = lst.get_list()

    assert len(result) == 1
    assert result[0].name == "Сыр"
    assert result[0].quantity == 600
    assert result[0].unit == "г"
    
def test_get_list_sorted():
    recipe = Recipe("Венские вафли в NY cafe")
    recipe.add_ingredient(Ingredient("Сахар", 100, "г"))
    recipe.add_ingredient(Ingredient("Мука миндальная", 200, "г"))
    recipe.add_ingredient(Ingredient("Яйца", 2, "шт"))
    lst = ShoppingList()
    lst.add_recipe(recipe, 1)
    result = lst.get_list()

    assert result[0].name == "Мука миндальная"
    assert result[1].name == "Сахар"
    assert result[2].name == "Яйца"    
        
def test_add_two_shopping_lst():
    recipe = Recipe("Вафельки")
    recipe.add_ingredient(Ingredient("Мука", 300, "г"))
    recipe2 = Recipe("Сырники")
    recipe2.add_ingredient(Ingredient("Яйца", 2, "шт"))

    lst1 = ShoppingList()
    lst2 = ShoppingList()
    lst1.add_recipe(recipe, 1)
    lst2.add_recipe(recipe2, 1)

    lst_final = lst1 + lst2
    result = lst_final.get_list()

    assert len(result) == 2
    assert result[0].name == "Мука"
    assert result[0].quantity == 300
    assert result[1].name == "Яйца"
    assert result[1].quantity == 2        
 
def test_add_two_shopping_lst_nochange():
    recipe = Recipe("Вафельки")
    recipe.add_ingredient(Ingredient("Мука", 300, "г"))
    recipe2 = Recipe("Сырники")
    recipe2.add_ingredient(Ingredient("Яйца", 2, "шт"))
    
    lst1 = ShoppingList()
    lst2 = ShoppingList()
    lst1.add_recipe(recipe, 1)
    lst2.add_recipe(recipe2, 1)

    lst_final = lst1 + lst2

    result1 = lst1.get_list()
    result2 = lst2.get_list()
    result_final = lst_final.get_list()
    
    assert len(result1) == 1
    assert result1[0].name == "Мука"
    assert len(result2) == 1
    assert result2[0].name == "Яйца"
    assert len(result_final) == 2         
      
        