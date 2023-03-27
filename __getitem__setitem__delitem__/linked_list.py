class StackObj:
    """для описания объектов стека"""

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """для управления стек-подобной структурой."""

    def __init__(self):
        # ссылка на первый объект стека (если стек пуст, то top = None).
        self.top = None
        self.__count_objects = 0

    def push(self, obj):
        """добавление объекта класса StackObj в конец стека"""
        last = self[self.__count_objects - 1] if self.__count_objects > 0 else None
        if last:
            last.next = obj

        if self.top is None:
            self.top = obj

        self.__count_objects += 1

    def pop(self):
        """извлечение последнего объекта с его удалением из стека;"""
        if self.__count_objects == 0:
            return None

        h = self[self.__count_objects - 2] if self.__count_objects > 1 else self[self.__count_objects - 1]
        last = self[self.__count_objects - 1]

        if self.__count_objects == 1:
            self.top = None
        else:
            h.next = None

        self.__count_objects -= 1
        return last

    def __check_index(self, index):
        if type(index) != int or not (0 <= index < self.__count_objects):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)

        count = 0
        h = self.top
        while h and count < item:
            h = h.next
            count += 1
        return h

    def __setitem__(self, key, value):
        self.__check_index(key)

        obj = self[key]
        prev = self[key - 1] if key > 0 else None

        value.next = obj.next
        if prev:
            prev.next = value


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data)  # obj3
print(st[1].data)  # new obj2
res = st[3]  # исключение IndexError
