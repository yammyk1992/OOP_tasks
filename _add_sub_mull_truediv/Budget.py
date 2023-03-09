class Budget:
    """для управления семейным бюджетом"""

    def __init__(self):
        self.budget = []

    def add_item(self, it):
        """добавление статьи расхода в бюджет (it - объект класса Item)"""
        self.budget.append(it.money)

    def remove_item(self, indx):
        """удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля)"""
        self.budget.pop(indx)

    def get_items(self):
        """возвращает список всех статей расходов (список из объектов класса Item)."""
        return self.budget


class Item:
    """пункт расходов бюджета."""

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return f"{self.money}"

    def __add__(self, other):
        print("сработало")
        if isinstance(other, Item):
            return self.money + other.money
        if isinstance(other, (float, int)):
            return self.money + other

    def __radd__(self, other):
        print("сработало")
        return self + other


it1 = Item("name", 1500)
it2 = Item("name2", 2000)
s = it1 + it2 + 5  # сумма для двух статей расходов

print(s)
my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
print(my_budget.get_items())

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
    print(s)
