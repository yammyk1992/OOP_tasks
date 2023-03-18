class Vector:
    def __init__(self, *args):
        self.numbers = [*args]

    def __add__(self, other):
        if len(self.numbers) != len(other.numbers):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*list(a + b for a, b in zip(self.numbers, other.numbers)))

    def __sub__(self, other):
        if len(self.numbers) != len(other.numbers):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*list(a - b for a, b in zip(self.numbers, other.numbers)))

    def __mul__(self, other):
        if len(self.numbers) != len(other.numbers):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*list(a * b for a, b in zip(self.numbers, other.numbers)))

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self.numbers = list(a + b for a, b in zip(self.numbers, other.numbers))
            return self
        self.numbers = list(i + other for i in self.numbers)
        return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            self.numbers = list(a - b for a, b in zip(self.numbers, other.numbers))
            return self
        self.numbers = list(i - other for i in self.numbers)
        return self

    def __eq__(self, other):
        return self.numbers == other.numbers


v1 = Vector(1, 2, 3)
v2 = Vector(1, 2, 3)

print((v1 + v2).numbers, "SUM")  # суммирование соответствующих координат векторов
print((v1 - v2).numbers, "-")  # вычитание соответствующих координат векторов
print((v1 * v2).numbers, "*")  # умножение соответствующих координат векторов

v1 += 10
print(v1.numbers)  # прибавление ко всем координатам вектора числа 10
v1 -= 10  # вычитание из всех координат вектора числа 10
print(v1.numbers)
v1 += v2
print(v1.numbers)
v2 -= v1
#
print(v1 == v2)  # True, если соответствующие координаты векторов равны
# v1 != v2  # True, если хотя бы одна пара координат векторов не совпадает

# При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными)
# координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
#
# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться
# исключение командой:
#
# raise ArithmeticError('размерности векторов не совпадают')
# P.S. В программе на экран выводить ничего не нужно, только объявить класс.
