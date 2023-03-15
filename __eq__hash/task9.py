class Dimensions:
    def __init__(self, a, b, c):
        if self.validator(a):
            self.a = a
        if self.validator(b):
            self.b = b
        if self.validator(c):
            self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    @staticmethod
    def validator(value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")

        return True


s_inp = '1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5'
lst_dims = [Dimensions(float(el.split()[0]), float(el.split()[1]), float(el.split()[-1])) for el in s_inp.split(';')]

sorted(lst_dims, key=lambda x: hash(x))
