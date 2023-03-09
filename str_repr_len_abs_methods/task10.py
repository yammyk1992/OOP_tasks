class PolyLine:
    def __init__(self, *args):
        self.__coord = [*args]

    def add_coord(self, x, y):
        self.__coord.append((x, y))

    def remove_coord(self, indx):
        self.__coord.pop(indx)

    def get_coords(self):
        return self.__coord


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(6, 7)
poly.remove_coord(0)
print(poly.get_coords())
