class Thing:
    id_instance = 1

    def __init__(self, id, name, price, weight=None, dims=None, memory=None, frm=None):
        """Увеличиваем id на 1 при создании объекта класса!!!"""
        self.id = Thing.id_instance if id is not None else id
        Thing.id_instance += 1
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm

    def get_data(self):
        return tuple(self.__dict__.values())[1:]


class Table(Thing):
    def __init__(self, name, price, weight=None, dims=None):
        super().__init__(id, name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory=None, frm=None):
        super().__init__(id, name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
