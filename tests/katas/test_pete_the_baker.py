from katas.pete_the_baker import cakes


class Recipes:
    def __init__(self):
        pass


class Ingredients:
    def __init__(self):
        pass


def test_cakes_returns_2():
    # arrange
    recipe = {
        "flour": 500,
        "sugar": 200,
        "eggs": 1
    }
    available = {
        "flour": 1200,
        "sugar": 1200,
        "eggs": 5,
        "milk": 200
    }

    # act
    result = cakes(recipe, available)

    # assert
    assert result == 2


def test_cakes_returns_0():
    # arrange
    recipe = {
        "apples": 3,
        "flour": 300,
        "sugar": 150,
        "milk": 100,
        "oil": 100
    }
    available = {
        "sugar": 500,
        "flour": 2000,
        "milk": 2000
    }

    # act
    result = cakes(recipe, available)

    # assert
    assert result == 0
