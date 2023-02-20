class LinkedList:
    def __init__(self):
        self.head = None  # ссылка на первый объект связного списка
        self.tail = None  # ссылка на последний объект связного списка

    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;"""
        obj.prev = self.tail
        # если tail уже ссылается на что-то
        if self.tail:
            # у tail - next будет ссылать на последний объект тоесть obj
            self.tail.next = obj
        # если tail == None, tail = добавленному объекту!!!
        self.tail = obj

        if not self.head:
            self.head = obj

    def __get_obj_by_index(self, indx):
        # берём самый первый объект
        h = self.head
        # счетчик объектов!
        count = 0
        while h and count < indx:
            # получаем объект по счетчику
            h = h.next
            count += 1
        return h

    def remove_obj(self, indx):
        """удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); индекс
        отсчитывается с нуля """
        obj = self.__get_obj_by_index(indx)
        # если объектов нет, то ничего не удаляем!
        if obj is None:
            return
        # убираем ссылки на объект и тем самым его очистит сборщик мусора
        p, n = obj.prev, obj.next
        # если есть ссылка на prev
        if p:
            # то obj.prev будет ссылаться на obj.next
            p.next = n
            # у нас obj.next = None
        if n:
            n.prev = p

        # если удаляемый объект первый, то head должен ссылаться на cледующий next объект
        if self.head == obj:
            self.head = n
        # если удаляемый объект первый, то tail должен ссылаться на предидущий prev объект
        if self.tail == obj:
            self.tail = p

    def __len__(self):
        """возвращает число объектов в связном списке"""
        n = 0
        h = self.head
        while h:
            n += 1
            # передаём объекты и считается счетчик!
            h = h.next
        return n

    def __call__(self, indx, *args, **kwargs):
        """возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом indx (в связном
        списке). """
        obj = self.__get_obj_by_index(indx)
        return obj.data if obj else ""


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        if type(value) in (ObjList, type(None)):
            self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if type(value) in (ObjList, type(None)):
            self.__next = value


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
print(n)
s = linked_lst(1)  # s = Balakirev
print(s)
