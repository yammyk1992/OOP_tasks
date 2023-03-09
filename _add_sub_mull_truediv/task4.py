class NewList:
    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._lst

    def __str__(self):
        return f"{self._lst}"

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("must be list or cls.NewList!")
        sc = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst, sc))

    @staticmethod
    def __diff_list(l1, l2):
        if len(l2) == 0:
            return l1
        sub = l2[:]
        return [x for x in l1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError("must be int or cls.Clock!")
        return NewList(self.__diff_list(other, self._lst))


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1)
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(lst1)
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print(res_2)
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
print(res_3)
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
