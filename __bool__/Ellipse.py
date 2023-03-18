class Ellipse:
    def __init__(self, *args):
        if args:
            self.x1, self.y1, self.x2, self.y2 = args[0], args[1], args[2], args[3]

    def __bool__(self):
        return len(self.__dict__) == 4

    def get_coords(self):
        if not ('x1', 'y1', 'x2', 'y2') in self.__dict__:
            return self.x1, self.y1, self.x2, self.y2
        raise AttributeError('нет координат для извлечения')


lst_geom = [*[Ellipse() for i in range(2)], *[Ellipse(1, 2, 3, 4) for y in range(2)]]
for i in lst_geom:
    if i:
        i.get_coords()
