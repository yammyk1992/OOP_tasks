# Магические методы арифметических операций!!!

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("seconds must be int")
        self.seconds = seconds % self.__DAY

    def get_seconds(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        "добавления 0 к минутам или секундам в правильном формате"
        return str(x).rjust(2, "0")

    def __add__(self, other):
        """для добавления. other - значение справа"""
        print("сработал метод _add__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("must be int or cls.Clock!")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)

    def __iadd__(self, other):
        """для добавления +="""
        print("Сработал метол __iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("must be int or cls.Clock!")

        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)


c = Clock(1000)
c2 = Clock(2000)
c3 = c + c2  # тоже самое что c.__add__(100)
print(c3.get_seconds())
# c.seconds = c.seconds + 100
print(c.get_seconds())
c += 100  # Сработал метол __iadd__
c += 200 # Сработал метол __iadd__
# для добавления арифметического метода без обращения к атрибутам
print(c.get_seconds())
