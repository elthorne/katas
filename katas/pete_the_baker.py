"""
Link: https://www.codewars.com/kata/525c65e51bf619685c000059

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and
returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts
(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects,
can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})

# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
"""


class Ingredients:
    def __init__(self, recipe, available):
        self.sufficient_ingredients = True

        if len(available) < len(recipe):
            self.sufficient_ingredients = False

        self.recipe = recipe
        self.available = available

    def bake(self):
        if not self.sufficient_ingredients:
            return 0

        return int(min(self.__divide_ingredients()))

    def __divide_ingredients(self):
        result = []
        for ingredient in self.recipe.keys():
            result.append(self.available[ingredient]/self.recipe[ingredient])
        return result


def cakes(recipe, available):
    return Ingredients(recipe, available).bake()

