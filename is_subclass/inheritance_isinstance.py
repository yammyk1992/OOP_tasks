class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

    def __str__(self):
        return f"{self.name}"


class Plants(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Flower(Flowering):
    """наследуется от Flowering и служит для описания цветка;"""
    pass


class Animals(Protists):
    pass


class Worms(Animals):
    pass


class Worm(Worms):
    """наследуется от Worms и служит для описания червей."""
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Person(Human):
    """наследуется от Human и служит для описания человека"""
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    """наследуется от Monkeys и служит для описания обезьян"""
    pass


lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8),
            Person("Балакирев", 88, 34), Person("Верховный жрец", 67.5, 45),
            Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
            Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]

# все объекты, относящиеся к животным (Animals);
lst_animals = [i for i in lst_objs if isinstance(i, Animals)]
print(lst_animals)

# все объекты, относящиеся к растениям (Plants);
lst_plants = [i for i in lst_objs if isinstance(i, Plants)]
print(lst_plants)

# все объекты, относящиеся к млекопитающим (Mammals).
lst_mammals = [i for i in lst_objs if isinstance(i, Mammals)]
print(lst_mammals)
