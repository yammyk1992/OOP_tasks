class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'инициализатор GEOM для {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Рисование линий')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        # super. возвращает объект поэтому нам ненадо писать в аргументах self
        super().__init__(x1, y1, x2, y2)
        print('инициализатор Rect')
        self.fill = fill

    def draw(self):
        print('Рисование прямоугольника')


r = Rect(1, 2, 3, 4)
l = Line(1, 24, 3, 45)
print(r.__dict__)

