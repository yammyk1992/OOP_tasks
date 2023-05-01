class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    # ограничивает создание локальных свойств и экономит память. Объекты этого класса не будут
    # содержать коллекцию __dict__
    # память узнать можно с помощью магического метода __sizeof__
    # ускоряет работу локальных свойств
    __slots__ = ('x', 'y', '__length')
    MAX_LENGTH = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


class Point3D(Point2D):
    # __slots__ не наследуется!!!
    # можно дополнить коллекцию __slots__

    __slots__ = 'z',
