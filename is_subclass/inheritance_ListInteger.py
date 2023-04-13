class ListInteger(list):
    def __init__(self, lst):
        for x in lst:
            if type(x) != int:
                raise TypeError('можно передавать только целочисленные значения')
        super().__init__(lst)

    def __setitem__(self, key, value):
        if type(value) != int:
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

    def append(self, item):  # real signature unknown
        """ Append object to the end of the list. """
        super().append(item)


s = ListInteger((1, 2, 3))
print(s[1], "S1")
s[1] = 10
print(s[1], "S1")
s.append(11)
print(s)
# s[0] = 10.5  # TypeError
