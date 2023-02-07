class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"[{self.data} ----> {self.next}]"

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        if isinstance(n, Node) or n is None:
            self.__next = n
        # print(f"пришел новый объект {n}")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, d):
        self.__data = d


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add_node(self, obj):
        print(obj, "OBJECT")

        if self.last:
            self.last.next = obj

        self.last = obj
        print(self.last, "LAAAAST")

        if self.head is None:
            self.head = obj

    def get_data(self):

        current_list = self.head
        lst = []
        while current_list:
            lst.append(current_list.data)
            current_list = current_list.next

        for i in lst:
            print(i, ">>>> ", end="")

        print()

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count


data = LinkedList()
data.add_node(Node("3"))
data.add_node(Node("4"))
data.add_node(Node("5"))
data.add_node(Node("6"))
data.get_data()
count = data.length()
print(count)
