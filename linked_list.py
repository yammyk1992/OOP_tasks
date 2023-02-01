class Node:
    """для описания объектов односвязного списка;"""

    def __init__(self, data=None, next=None):
        self.__data = data
        self.__next = next

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


class LinkedList:

    def __init__(self):
        self.head = None

    def append_data(self, data):
        """добавление в конец нашего Linked list"""
        new_node = Node(data)
        current_node = self.head
        if current_node is None:
            self.head = new_node
            return
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def show(self):
        """вывод на экран добавленных элементов"""
        current_node = self.head
        output = ""
        while current_node is not None:
            output += str(current_node.data) + " --> "
            current_node = current_node.next
        print(output)

    def count_element(self):
        """подсчет всех элементов"""
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        print(count)

    def push_front(self, data):
        """добавление нового объекта в начало листа"""
        new_node = Node(data)
        first_node = self.head
        new_node.next = first_node
        self.head = new_node

    def remove_last_element(self):
        """удаление последнего элемента в листе"""
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

    def remove_first_element(self):
        """удаление первого элемента в листе"""
        current_node = self.head
        self.head = current_node.next

    def get_value_with_index(self, index):
        """получение значения по индексу"""
        count = 0
        current_node = self.head
        while current_node is not None:
            if count == index:
                return current_node.data
            count += 1
            current_node = current_node.next
        raise ValueError("INDEX OUT OF RANGE")

    def insert_element_with_index(self, index, data):
        """вставка элемент по определённому индексу"""
        new_node = Node(data)
        current_node = self.head
        count = 0
        while current_node.next is not None:
            if index == 0:
                self.push_front(data)
                return
            elif count + 1 == index:
                next_node_after_current_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node_after_current_node
                return
            count += 1
            current_node = current_node.next
        raise ValueError("INDEX OUT OF RANGE")

    def remove_element_with_index(self, index):
        """удаление значения по индексу"""
        count = 0
        current_node = self.head
        while current_node.next is not None:
            if index == 0:
                return
            elif count + 1 == index:
                remove_element = current_node.next
                element_after_removed = remove_element.next
                current_node.next = element_after_removed
                return
            count += 1
            current_node = current_node.next
        raise ValueError("INDEX OUT OF RANGE")


my_list = LinkedList()
my_list.append_data(2)
my_list.append_data(4)
my_list.append_data(6)
my_list.append_data(8)
my_list.append_data(10)

# print(my_list.get_value_with_index(3))
# my_list.push_front(20)

# my_list.insert_element_with_index(25, 9)
my_list.show()
my_list.remove_element_with_index(1)
my_list.show()
# my_list.remove_last_element()
# my_list.remove_first_element()
# my_list.show()
# my_list.count_element()
