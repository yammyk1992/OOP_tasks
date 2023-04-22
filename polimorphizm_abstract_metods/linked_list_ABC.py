from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        """добавление объекта в конец стека"""
        pass

    @abstractmethod
    def pop_back(self):
        """удаление последнего объекта из стека."""
        pass


class Stack(StackInterface):
    def __init__(self):
        # ссылка на первый объект стека (если стек пуст, то top = None).
        self._top = None
        self.last = None

    def push_back(self, obj):
        """добавление объекта класса StackObj в конец стека"""
        if self.last:
            self.last.next = obj

        if self._top is None:
            self._top = obj

        self._top.next = obj
        self.last = obj

    def pop_back(self):
        """извлечение последнего объекта с его удалением из стека;"""
        h = self._top
        last = self.last
        if h is None:
            return
        while h.next and h.next != self.last:
            h = h.next

        if self._top == self.last:
            self._top = self.last = None
        else:
            h.next = None
            self.last = h
        return last


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, n):
        self._next = n

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, d):
        self._data = d


st = Stack()
st.push_back(StackObj("obj 1"))

obj = StackObj("obj 2")

st.push_back(obj)
del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print(del_obj, "DEL OBJ")
