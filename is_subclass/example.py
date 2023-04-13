class Geom:
    pass


class Line(Geom):
    pass


g = Geom()
l = Line()
# работает только с классами а не с экземплярами. Проверяет является ли класс подклассом другого класса
print(issubclass(Line, Geom))
print(l.__class__)
print(g)
print(Geom.__name__)


class Vector(list):
    def __str__(self):
        return ' '.join(map(str, self))


v = Vector([1, 2, 3])
print(v)
