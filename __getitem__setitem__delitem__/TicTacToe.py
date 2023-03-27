class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return True if self.is_free else False


class TicTacToe:
    def __init__(self):
        self.n = 3
        self.pole = tuple(tuple(Cell() for _ in range(self.n)) for _ in range(self.n))

    def clear(self):
        """очистка игрового поля (все клетки заполняются нулями и переводятся в закрытое состояние)"""
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = 0

    def __check_value(self, item):
        if type(item) != tuple or len(item) != 2:
            raise IndexError('неверный индекс клетки')
        if any(not (0 <= x < self.n) for x in item if type(x) != slice):
            raise IndexError('неверный индекс клетки')

    def __setitem__(self, key, value):
        self.__check_value(key)
        # если проверка прошла успешно то мы распаковываем tuple()
        r, c = key

        if self.pole[r][c]:
            self.pole[r][c].value = value
            self.pole[r][c].is_free = False
        else:
            raise ValueError('клетка уже занята')

    def __getitem__(self, item):
        self.__check_value(item)
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(self.n))
        if type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(self.n))

        return self.pole[r][c].value


game = TicTacToe()
game.clear()
game[0, 0] = 1
game[1, 0] = 2
print(game.pole)
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
game[3, 2] = 2  # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
v1 = game[0, :]  # 1, 0, 0
v2 = game[:, 0]  # 1, 2, 0
