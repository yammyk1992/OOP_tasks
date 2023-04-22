class Track:
    def __init__(self, *args):
        self.__points = [*args]

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        """добавление новой точки в конец маршрута (pt - объект класса PointTrack);"""
        self.__points.append(pt)

    def add_front(self, pt):
        """добавление новой точки в начало маршрута (pt - объект класса PointTrack);"""
        self.__points.insert(0, pt)

    def pop_back(self):
        """удаление последней точки из маршрута;"""
        self.__points.pop(-1)

    def pop_front(self):
        """ удаление первой точки из маршрута."""
        self.__points.pop(0)


class PointTrack:
    def __init__(self, x, y):
        self.check_value(x)
        self.x = x
        self.check_value(y)
        self.y = y

    def check_value(self, value):
        if type(value) not in (int, float):
            raise TypeError('координаты должны быть числами')
        return value

    def __str__(self):
        return f"PointTrack: {self.x}, {self.y}"


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
