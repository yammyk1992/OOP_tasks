from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.__real = real
        self.__img = img

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")
        self.__img = value

    def __abs__(self):
        return sqrt(self.real * self.real + self.img * self.img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4

c_abs = abs(cmp)
print(c_abs)

