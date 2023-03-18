class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return False if pow(self.x2 - self.x1, 2) + pow(self.x2 - self.y1, 2) * 0.5 < 1 else True


line = Line(0, 0, 3, 4)
b = bool(line)
print(b)
