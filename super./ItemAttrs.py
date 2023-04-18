class ItemAttrs:
    def __init__(self, lst):
        self.lst = []

    def __getitem__(self, item):
        return self.lst[item]

    def __setitem__(self, key, value):
        self.lst[key] = value


class Point(ItemAttrs):
    def __init__(self, x, y, lst=None):
        super().__init__(lst)
        self.x = x
        self.y = y
        self.lst = [x, y]


pt = Point(1, 2.5)
x = pt[0]  # 1
print(x)
y = pt[1]  # 2.5
pt[0] = 10
print(pt[0])
