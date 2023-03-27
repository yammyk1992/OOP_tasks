class IntegerValue:
    """дескриптор данных для работы с целыми числами."""

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise ValueError('возможны только целочисленные значения')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_coord(value)
        instance.__dict__[self.name] = value


class TableValues:
    """для работы с таблицей в целом;"""

    def __init__(self, rows, cols, cell=None):
        self.rows = rows
        self.cols = cols
        if cell is None:
            raise ValueError('параметр cell не указан')
        else:
            self.cells = tuple(tuple(cell() for _ in range(self.cols)) for _ in range(self.rows))

    def __check_index(self, index):
        r, c = index
        if type(r) != int or not (0 <= r < self.rows) or type(c) != int or not (0 <= c < self.cols):
            raise IndexError

    def __getitem__(self, item):
        self.__check_index(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.cells[key[0]][key[1]].value = value


class CellInteger:
    """для операций с целыми числами;"""

    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
table[0, 0] = 1.45  # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
