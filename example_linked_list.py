class Node:
    def __init__(self, data):
        self.next = None  # сохраняет ссылку на следующий узел
        self.data = data  # data будет хранить фактические данные для узла
        self.prev = None  # сохраняет ссылку на предыдущий узел в двусвязном списке

    # def __str__(self):
    #     return f"НОВЫЕ ДАННЫЕ ПРИШЛИ {self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # начальный узел

    def insert_in_emptylist(self, data):
        """Вставка элементов в пустой список"""
        if self.head is None:
            new_node = Node(data)
            print(new_node, ">>>>>>")
            self.head = new_node
        # else:
        #     # print("list is not empty")

    def insert_at_start(self, data):
        """Вставка элементов в начале"""
        if self.head is None:
            self.insert_in_emptylist(data)
            # print("ОТРАБОТАЛА ВСТАВКА В ПУСТОЙ УЗЕЛ")
            return
        new_node = Node(data)
        new_node.prev = self.head
        new_node.next = new_node
        self.head = new_node
        # print("ВСТАВЛЕНО в НАЧАЛО")

    def insert_at_end(self, data):
        """Вставка элементов в конце"""
        if self.head is None:
            self.insert_in_emptylist(data)
            print("ОТРАБОТАЛА ВСТАВКА В ПУСТОЙ УЗЕЛ")
            return
        print(self.head, "НЕ ПУСТОЙ")
        n = self.head
        while n.next is not None:
            print(n.next, "N NEEEEXT")
            n = n.prev
            print(n, "ПРЕДВЕДУЩИЕ ЗНАЧЕНИЯ")
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
        print(">>>>> прошлое", new_node.prev.data, ">>>>>", n.next.data, " >>>>>>> ПОСЛЕДНЕЕ ДОБАВЛЕННОЕ")

    def insert_after_item(self, x, data):
        if self.head is None:
            return
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("Item not in the list")
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.prev is not None:
                    n.next.prev = new_node
                n.next = new_node


h = DoublyLinkedList()
h.insert_in_emptylist("2")
h.insert_in_emptylist("3")  # здесь уже узел не пустой!
h.insert_at_start("2")
h.insert_at_end("5")
h.insert_after_item("2", "8")
