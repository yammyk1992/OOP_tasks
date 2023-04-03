class Stack:

    def __init__(self):
        self.top = None
        self.last = None
        self.count_obj = 0

    def push_back(self, obj):
        """для добавления нового объекта obj в конец стека;"""
        if self.top is None:
            self.top = obj
        else:
            self.last.next = obj
        self.last = obj

    def push_front(self, obj):
        """для добавления нового объекта obj в начало стека."""
        if self.top is None:
            self.last = self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next

    def __len__(self):
        return sum(1 for _ in self)

    def _get_object(self, indx):
        if type(indx) != int or not (0 <= indx < len(self)):
            raise IndexError('неверный индекс')
        for i, obj in enumerate(self):
            if i == indx:
                return obj

    def __getitem__(self, item):
        return self._get_object(item).data

    def __setitem__(self, key, value):
        self._get_object(key).data = value


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


st = Stack()

st[1] = 2  # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[2]  # получение данных из объекта стека по индексу
n = len(st)  # получение общего числа объектов стека

for obj in st:  # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
