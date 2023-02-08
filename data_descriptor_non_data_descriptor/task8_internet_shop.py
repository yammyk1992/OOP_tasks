class StringValue:

    def __init__(self, min_length=2, max_length=50):
        self.max_length = max_length
        self.min_length = min_length

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)

    def validate(self, string):
        return type(string) == str and self.max_length >= len(string) >= self.min_length


class PriceValue:
    def __init__(self, max_value=10000):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        print("INSTAAAANCE")
        print("OWNER")
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)

    def validate(self, value):
        if isinstance(value, (int, float)) and value <= self.max_value:
            return True
        else:
            raise ValueError("Превысили")


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name):
        self.name = str(name)
        self.goods = []

    def add_product(self, product):
        """добавление товара в магазин (в конец списка goods);"""
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        """удаление товара из магазина (из списка goods)"""
        self.goods.pop(self.goods.index(product))


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 50))
for p in shop.goods:
    print(f"{p.__name}: {p.__price}")
