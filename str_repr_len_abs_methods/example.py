# class Cat:
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old
#
#     def __repr__(self):
#         """Для вывода отладочной информации об объекте класса для разработчиков"""
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         """Информация для пользователя об объекте класса(например для print, str)"""
#         print("Метод str сработал далее --->")
#         return f"{self.name} ему {self.old} лет"
#
#
# cat = Cat("Васька", 25)
# print(cat)

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        """Позволяет применять функцию len к экземплярам класса"""
        return len(self.__coords)

    def __abs__(self):
        """Позволяет применять функцию abc к экземплярам класса"""
        return list(map(abs, self.__coords))


p = Point(1, -2)
print(len(p))
print(abs(p))
