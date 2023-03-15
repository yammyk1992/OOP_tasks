from math import sqrt


class Integer:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        print("Сработал геттер", owner, "OWNER")
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = Integer()
    b = Integer()
    c = Integer()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return self.a + self.b + self.c

    # позволяет вызывать объекты класса подобно функциям, в котором определен метод __call__()
    def __call__(self, *args, **kwargs):
        a, b, c = self.a, self.b, self.c
        p = 0.5 * (a + b + c)
        return sqrt(p * (p - a) * (p - b) * (p - c))

    def __setattr__(self, key, value):
        """Вызывается при изменении аттрибута key класса"""
        if (key == "a" and not self.validate_triangle(value, self.b, self.c)) or \
                (key == "b" and not self.validate_triangle(self.a, value, self.c)) or \
                (key == "c" and not self.validate_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

        object.__setattr__(self, key, value)

    def validate_triangle(self, a, b, c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b

        return True


tr = Triangle(3, 3, 3)
len(tr)
tr()
