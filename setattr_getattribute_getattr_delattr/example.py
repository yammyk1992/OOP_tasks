class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        """Автоматически вызывается при получении аттрибута класса с именем item """
        if item == "x":
            raise ValueError("Доступ запрещен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """Вызывается при изменении аттрибута key класса"""
        if key == "z":
            raise AttributeError("Доступ запрещен")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        """Вызывается когда мы обращаемся к не существующему аттрибуту класса"""
        print(f"ключа {item} не существует!!!")
        return False

    def __delattr__(self, item):
        """Вызывается при удаление аттрибута класса!"""
        print(f"Удалили аттрибут {item}")
        object.__delattr__(self, item)


pt = Point(1, 2)
pt2 = Point(10, 20)
pt.x = "5"
print(pt.value)
print(pt.__dict__)
del pt.x
print(pt.__dict__)
