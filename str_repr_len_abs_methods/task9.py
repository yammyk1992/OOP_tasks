class Recipe:
    """класс Recipe для представления рецептов"""

    def __init__(self, *args):
        self.recipe = list(args)

    def add_ingredient(self, ing):
        """добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец)"""
        self.recipe.append(ing)

    def remove_ingredient(self, ing):
        """удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;"""
        self.recipe.remove(ing)

    def get_ingredients(self):
        return tuple(self.recipe)

    def __len__(self):
        return len(self.recipe)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}"


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
# здесь сработал метод __str__
print(*[i for i in ings])
# без него просто показаны объекты!
n = len(recipe)
print(n)  # n = 3
