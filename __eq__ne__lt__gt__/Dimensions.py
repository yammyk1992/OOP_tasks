class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, i):
        if i in range(self.MIN_DIMENSION, self.MAX_DIMENSION):
            self.__a = i

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, i):
        if i in range(self.MIN_DIMENSION, self.MAX_DIMENSION):
            self.__b = i

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, i):
        if i in range(self.MIN_DIMENSION, self.MAX_DIMENSION):
            self.__c = i

    def validate_value(self, value):
        return value.a * value.b * value.c

    def __ge__(self, other):
        return self.validate_value(self) >= self.validate_value(other)

    def __gt__(self, other):
        return self.validate_value(self) > self.validate_value(other)

    def __le__(self, other):
        return self.validate_value(self) <= self.validate_value(other)

    def __lt__(self, other):
        return self.validate_value(self) < self.validate_value(other)


class ShopItem:
    """Товар"""

    def __init__(self, name, price, dim):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem("кеды", 1024, Dimensions(40, 30, 120)), ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
            ShopItem("холодильник", 40000, Dimensions(2000, 600, 500)),
            ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)  # x.dim если в классе ShopItem self.dim
dim1 = Dimensions(1, 2, 3)
dim2 = Dimensions(2, 3, 4)
print(dim1 >= dim2)   # True, если объем dim1 больше или равен объему dim2
print(dim1 > dim2)    # True, если объем dim1 больше объема dim2
print(dim1 <= dim2)   # True, если объем dim1 меньше или равен объему dim2
print(dim1 < dim2)    # True, если объем dim1 меньше объема dim2
