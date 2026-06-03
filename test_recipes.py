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
