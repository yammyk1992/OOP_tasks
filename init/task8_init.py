class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        """добавление в корзину товара, представленного объектом gd"""
        self.goods.append(gd)

    def remove(self, indx):
        """удаление из корзины товара по индексу indx;"""
        self.goods.pop(indx)

    def get_list(self):
        """получение из корзины товаров в виде списка из строк:"""
        return [f"{x.name}: {x.price}" for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()

gd = TV("LG", 2000)
cart.add(gd)
gd1 = TV("SAMSUNG", 5000)
cart.add(gd1)

tb = Table("table", 400)
cart.add(tb)
tb1 = Table("table1", 500)
cart.add(tb1)

nb = Notebook("mac", 1000)
cart.add(nb)
nb1 = Notebook("mac pro", 10000)
cart.add(nb1)

cp = Cup("mug", 200)
cart.add(cp)

print(cart.get_list())
