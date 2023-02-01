class StackObj:
    """для описания объектов односвязного списка;"""

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        if isinstance(n, StackObj) or n is None:
            self.__next = n

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data = d


class Stack:
    """для управления односвязным списком."""

    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        """ добавление объекта класса StackObj в конец односвязного списка;"""
        if self.last:
            self.last.next = obj

        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        """извлечение последнего объекта с его удалением из односвязного списка;"""
        current_node = self.top
        if current_node is None:
            return
        while current_node and current_node.next != self.last:
            current_node = current_node.next
        if current_node:
            current_node.next = None
        last = self.last
        self.last = current_node
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        """получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого
        объекта в порядке их добавления, или пустой список, если объектов нет). """
        """вывод на экран добавленных элементов"""
        current_node = self.top
        output = []
        while current_node:
            output.append(current_node.data)
            current_node = current_node.next
        return output


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
print(st.get_data())
