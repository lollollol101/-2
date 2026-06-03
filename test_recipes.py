from main import Ingredient, Recipe, ShoppingList
import pytest

@pytest.fixture
def cinnamon():
    return Ingredient('Корица', 2, 'г')

def test_create_ingredient(cinnamon):
    assert cinnamon.name=='Корица'
    assert cinnamon.quantity==2.0
    assert cinnamon.unit=='г'

def test_ingredient_str(cinnamon):
    assert str(cinnamon)=='Корица: 2.0 г'

def test_ingredient_eq(cinnamon):
    assert cinnamon==Ingredient('Корица', 5, 'г')
    assert cinnamon!=Ingredient('Кардамон', 2, 'г')
    assert cinnamon!=Ingredient('Корица', 2, 'не г')


@pytest.fixture
def recipe_1():
    return Recipe('Нечто', [Ingredient('Сахар', 3, 'г'), Ingredient('Соль', 2, 'г')])

def test_create_recipe(recipe_1):
    assert recipe_1.title == 'Нечто'
    assert len(recipe_1.ingredients) == 2

def test_add_ingredient():
    recipe = Recipe('Что-то', [])
    ingredient = Ingredient('Что-то вкусное', 3, 'шт')
    recipe.add_ingredient(ingredient)
    assert len(recipe) == 1
    assert recipe.ingredients[0].name == 'Что-то вкусное'

def test_add_ingredient_duplicate():
    recipe = Recipe('Что-то', [])
    ingredient = Ingredient('Что-то вкусное', 3, 'шт')
    recipe.add_ingredient(ingredient)
    ingredient_dup = Ingredient('Что-то вкусное', 4, 'шт')
    recipe.add_ingredient(ingredient_dup)
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 7

def test_recipe_scale(recipe_1):
    recipe_1_new = recipe_1.scale(5)
    assert recipe_1_new is not recipe_1
    for i in recipe_1.ingredients:
        if i.name == 'Сахар':
            assert i.quantity == 3
        if i.name == 'Соль':
            assert i.quantity == 2
    for i in recipe_1_new.ingredients:
        if i.name == 'Сахар':
            assert i.quantity == 15
        if i.name == 'Соль':
            assert i.quantity == 10
    with pytest.raises(ValueError):
        recipe_1.scale(-2)
    with pytest.raises(ValueError):
        recipe_1.scale(0)

def test_recipe_len(recipe_1):
    assert len(recipe_1) == 2