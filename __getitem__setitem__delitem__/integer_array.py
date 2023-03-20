class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, item):
        if not isinstance(item, int) and item < 0:
            raise ValueError('должно быть целое число')
        self.__value = item

    def __repr__(self):
        return str(self.__value)


class Array:
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.__array = [self.__cell() for _ in range(max_length)]

    def __getitem__(self, item):
        if type(item) != int and item >= self.__max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')
        return self.__array[item].value

    def __setitem__(self, key, value):
        self.__array[key].value = value

    def __repr__(self):
        return " ".join(map(str, self.__array))


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел

# ar_int[1] = 10.5  # должно генерироваться исключение ValueError
# ar_int[10] = 1  # должно генерироваться исключение IndexError
