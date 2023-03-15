class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        print("__bool__")
        return self.x == self.y


p = Point(1, 10)
print(bool(p))
if p:
    print("объект p даёт true")
else:
    print("объект p даёт false")
