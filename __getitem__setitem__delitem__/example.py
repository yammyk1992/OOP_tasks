class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        """Вызывается когда нужно получить значение из списка напрямую в объекте, в item прилетает индекс"""
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("неверный индекс")

    def __setitem__(self, key, value):
        """Вызывается когда присваевается значение по индексу списка напрямую в объекте, в key прилетает индекс,
        в value значение """
        if not isinstance(key, int) or key < 0:
            raise TypeError("key must be an integer and > 0")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            print(off)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        """Вызывается когда происходит удаление того или иного элемента из списка"""
        if not isinstance(key, int):
            raise TypeError("key must be an integer and > 0")

        del self.marks[key]


s1 = Student("Вася", [4, 5, 6, 2, 123])
s1[12] = 16
del s1[12]
print(s1.marks)
