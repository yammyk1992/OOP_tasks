class Cell:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.__type_data = type_data
        self.__rows = rows
        self.__cols = cols
        self.__cells = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))

    def check_value(self, value):
        r, c, = value
        if not (0 <= r < self.__rows) or not (0 <= c < self.__cols):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_value(item)
        r, c = item
        return self.__cells[r][c].data

    def __setitem__(self, key, value):
        self.check_value(key)
        if type(value) != self.__type_data:
            raise TypeError('неверный тип присваиваемых данных')
        r, c = key
        self.__cells[r][c].data = value

    def __iter__(self):
        for row in self.__cells:
            yield (x.data for x in row)


table = TableValues(2, 3)
table[2, 3] = 5  # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[3, 2]  # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row:  # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()
