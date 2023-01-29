class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        pass

    def remove_obj(self):
        pass

    def get_data(self):
        pass


class ObjList:

    def __init__(self, next, prev, data):
        self.__next = next
        self.__prev = prev
        self.__data = data