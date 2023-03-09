class ListMath:
    def __init__(self, lst_math=None):
        self._lst_math = lst_math[:] if lst_math else []

    def __add__(self, other):
        return ListMath([i + other for i in self._lst_math if type(i) in (float, int)])

    def __radd__(self, other):
        return ListMath([other + i for i in self._lst_math if type(i) in (float, int)])

    def __iadd__(self, other):
        self._lst_math = [i + other for i in self._lst_math if type(i) in (float, int)]
        return self

    def __sub__(self, other):
        return ListMath([i - other for i in self._lst_math if type(i) in (float, int)])

    def __rsub__(self, other):
        return ListMath([other - i for i in self._lst_math if type(i) in (float, int)])

    def __isub__(self, other):
        self._lst_math = [i - other for i in self._lst_math if type(i) in (float, int)]
        return self

    def __mul__(self, other):
        return ListMath([i * other for i in self._lst_math if type(i) in (float, int)])

    def __rmul__(self, other):
        return ListMath([other * i for i in self._lst_math if type(i) in (float, int)])

    def __imul__(self, other):
        self._lst_math = [i * other for i in self._lst_math if type(i) in (float, int)]
        return self

    def __truediv__(self, other):
        return ListMath([i / other for i in self._lst_math if type(i) in (float, int)])

    def __rtruediv__(self, other):
        return ListMath([other / i for i in self._lst_math if type(i) in (float, int)])

    def __itruediv__(self, other):
        self._lst_math = [i / other for i in self._lst_math if type(i) in (float, int)]
        return self


lst = ListMath([1, "abc", -5, 7.68, True])  # ListMath: [1, -5, 7.68]
# lst = lst + 76
# print(lst)
# lst = 6.5 + lst
# print(lst)
# lst += 76.7
# print(lst)
# lst1 = lst - 76  # вычитание из каждого числа списка определенного числа
# print(lst1)
# # lst = 7.0 - lst  # вычитание из числа каждого числа списка
# # print(lst)
# lst -= 76.3
# print(lst)
# lst = lst * 5  # умножение каждого числа списка на указанное число (в данном случае на 5)
# print(lst)
# lst = 5 * lst  # умножение каждого числа списка на указанное число (в данном случае на 5)
# print(lst)

# lst = lst / 13  # деление каждого числа списка на указанное число (в данном случае на 13)
# print(lst)
# lst *= 5.54
# print(lst)
lst = 3 / lst  # деление числа на каждый элемент списка
print(lst)
