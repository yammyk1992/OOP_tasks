class Body:
    def __init__(self, name: str, ro: (int, float), volume: (int, float)):
        self.name = name  # название тела (строка)
        self.ro = ro  # плотность тела (число: вещественное или целочисленное)
        self.volume = volume  # объем тела  (число: вещественное или целочисленное)

    @staticmethod
    def validate(ro, volume):
        return ro * volume

    def __gt__(self, other):
        return self.validate(self.ro, self.volume) > other.validate(other.ro, other.volume)

    def __eq__(self, other):
        if type(other) in (int, float):
            return self.validate(self.ro, self.volume) == other
        else:
            return self.validate(self.ro, self.volume) == other.validate(other.ro, other.volume)

    def __lt__(self, other):
        return self.validate(self.ro, self.volume) < other


body1 = Body("тело", 24.4, 33.2)
body2 = Body("тело2", 24.4, 33.2)
print(body1 > body2)
print(body1 == body2)
print(body1 < 10)
print(body2 == 5)
