class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def draw(self):
        print('Рисование прямоугольника')


g = Geom()
print(g.name)
r = Rect()
r.set_coords(1, 2, 3, 4)
l = Line()
l.set_coords(2, 3, 4, 5)
setattr(l, 'name', 'Line')
print(l.name)
l.draw()
setattr(r, 'name', 'Rect')
print(r.name)
print(l.__dict__)
print(r.__dict__)
