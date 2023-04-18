class StringDigit(str):
    def __init__(self, s):
        self.check(s)
        self.s = s

    def __add__(self, other):
        return StringDigit(self.s + other)

    def __radd__(self, other):
        return StringDigit(other + self.s)

    @staticmethod
    def check(string):
        if not all(i.isdigit() for i in string):
            raise ValueError("в строке должны быть только цифры")
        return string


sd = StringDigit('1231241124')
sd = sd + "123"
sd = "123" + sd
sd = "vvv" + sd # ValueError
print(sd)
