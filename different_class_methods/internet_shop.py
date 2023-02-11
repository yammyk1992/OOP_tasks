class Product:
    id_instance = 1
    d_types = {'name': (str,), 'weight': (int, float), 'price': (int, float)}

    def __init__(self, name, weight, price):
        """Увеличиваем id на 1 при создании объекта класса!!!"""
        self.id = Product.id_instance
        Product.id_instance += 1

        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in self.d_types and type(value) in self.d_types[key]:
            if (key == "price" or key == "weight") and value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in self.d_types:
            raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        """Вызывается при удаление аттрибута класса!"""
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        if product in self.goods:
            self.goods.remove(product)


# # shop = Shop(название магазина)
# p = Product("название", 25, 300)
# p1 = Product("название", 22, 303)
# print(p.__dict__)
# print(p1.__dict__)
# print(Product.__dict__)
shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.id} {p.name}, {p.weight}, {p.price} ")
