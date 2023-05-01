class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinsLog:
    ID = 1

    def __init__(self):
        super().__init__()
        print("MixinLog")
        self.id = MixinsLog.ID
        MixinsLog.ID += 1

    def save_sell_log(self):
        print(f"id - {self.ID}: товар был продан в 00 часов")

    def print_info(self):
        print(f"Вызов из класса MixinsLog")


class NoteBook(Goods, MixinsLog):
    def print_info(self):
        MixinsLog.print_info(self)


notebook = NoteBook('Acer', 2.5, 50000)
notebook.print_info()
notebook.save_sell_log()
print(NoteBook.__mro__)
