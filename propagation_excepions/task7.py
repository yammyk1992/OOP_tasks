digits = list(map(float, input().split()))


class TupleLimit(tuple):
    def __init__(self, lst, max_length):
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')
        self.lst = lst
        self.max_length = max_length

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __str__(self):
        return f"{self.lst}"

    def __repr__(self):
        return f"{self.lst}"


try:
    tl = TupleLimit(digits, 5)
except ValueError as v:
    print(v)
else:
    print(*tl.lst)
