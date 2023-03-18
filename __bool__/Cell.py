from random import randint


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print("NEW")
        """Singleton pattern for add 1 object"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        GamePole._instance = None

    def __init__(self, N, M, total_mines):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.init_pole()

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for row in self.__pole_cells:
            for x in row:
                x.is_open = True
                x.is_mine = False

        m = 0
        while m < self.total_mines:
            i = randint(0, self.N - 1)
            j = randint(0, self.M - 1)
            if self.__pole_cells[i][j].is_mine:
                continue
            self.__pole_cells[i][j].is_mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.N):
            for y in range(self.M):
                if not self.pole[x][y].is_mine:
                    mines = sum((self.pole[x + i][y + j].is_mine for i, j in indx if
                                 0 <= x + i < self.N and 0 <= y + j < self.M))
                    self.pole[x][y].number = mines

    def open_cell(self, i, j):
        if not 0 <= i < self.N or not 0 <= j < self.M:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            print(*map(lambda x: "#" if not x.is_open else x.number if not x.is_mine else "*", row))


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def is_number(self):
        return self.__number

    @is_number.setter
    def is_number(self, value):
        if type(value) != int or value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open


p = GamePole(10, 12, 10)
p.show_pole()


