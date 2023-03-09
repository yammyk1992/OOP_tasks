class Stack:
    def __init__(self):
        self.top = None  # ссылка на первый объект односвязного списка (если объектов нет, то top = None).
        self.__last_ = None  # ссылка на последний объект

    def push_back(self, obj):
        """добавление объекта класса StackObj в конец односвязного списка;"""
        if self.__last_:
            self.__last_.next = obj
        self.__last_ = obj

        if self.top is None:
            self.top = obj

    def pop_back(self):
        """удаление последнего объекта из односвязного списка."""
        h = self.top
        if h is None:
            return
        while h.next and h.next != self.__last_:
            h = h.next

        if self.top == self.__last_:
            self.top = self.__last_ = None
        else:
            h.next = None
            self.__last_ = h

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        for x in other:
            self.push_back(StackObj(x))
        return self

    def __imul__(self, other):
        return self.__mul__(other)


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, d):
        self.__next = d


obj = StackObj("data")
st = Stack()
# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj
st += obj

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']
