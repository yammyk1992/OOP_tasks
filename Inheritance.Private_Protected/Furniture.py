class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self._name = name
        self.__verify_weight(weight)
        self._weight = weight

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.__verify_name(value)
        self._name = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self.__verify_weight(value)
        self._weight = value

    def __verify_name(self, name):
        """для проверки корректности имени;"""
        if type(name) != str:
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        """для проверки корректности веса"""
        if weight <= 0:
            raise TypeError('вес должен быть положительным числом')


class Closet(Furniture):
    """для представления шкафов;"""

    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Chair(Furniture):
    """для представления стульев;"""

    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Table(Furniture):
    """для представления столов."""

    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return tuple(self.__dict__.values())

cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
