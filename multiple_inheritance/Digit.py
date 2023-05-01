class Digit:
    def __init__(self, value):
        if type(value) not in (int, float):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        if type(value) is not int:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Float(Digit):
    def __init__(self, value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Positive(Digit):
    def __init__(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class Negative(Digit):
    def __init__(self, value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)


class PrimeNumber(Integer, Positive):
    """простые числа"""
    pass


class FloatPositive(Float, Positive):
    pass


n = Negative(-5)
digits = [PrimeNumber(5), PrimeNumber(4), PrimeNumber(2), FloatPositive(1.2), FloatPositive(1.3), FloatPositive(1.4),
          FloatPositive(1.5), FloatPositive(1.6)]
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
print(lst_positive)
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
print(lst_float)
