class StackObj:
    """для описания объектов односвязного списка;"""

    def __init__(self, d):
        self.__data = d
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data = d


class Stack:
    """для управления односвязным списком."""

    def __init__(self, top=None):
        if top is not None:
            self.top = []

    def push(self, obj):
        """ добавление объекта класса StackObj в конец односвязного списка;"""
        self.top.append(obj.data)

    def pop(self):
        """извлечение последнего объекта с его удалением из односвязного списка;"""
        self.top.pop()

    def get_data(self):
        """получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого
        объекта в порядке их добавления, или пустой список, если объектов нет). """
        return self.top


# obj = StackObj(данные)
# st = Stack() # создание объекта односвязного списка


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()  # ['obj1', 'obj2']
print(*res)
