class Point:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pt = Point(4, 5)
pt.clone()
