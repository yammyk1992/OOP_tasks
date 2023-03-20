class Track:
    def __init__(self, x, y):

        self.start = (x, y)
        self.all_points = []

    def add_point(self, x, y, speed):
        """ добавление новой точки маршрута (линейный сегмент), который можно пройти со средней скоростью speed."""
        new_points = [(x, y), speed]
        self.all_points.append(new_points)

    def __setitem__(self, key, value):
        self.all_points[key][1] = value

    def __getitem__(self, item):
        if 0 <= item < len(self.all_points):
            return self.all_points[item]
        else:
            raise IndexError("неверный индекс")


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2
print(tr.all_points)
tr[2] = 60
print(tr[2])
#
c, s = tr[2]
print(c, s)

# res = tr[3]  # IndexError
# print(res)
