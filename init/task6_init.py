# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def get_str_data(self):
        return " ".join(map(str, self.data))

    def set_data(self, data):
        self.data = data[:]

    def show_table(self):
        if self.is_show:
            print(self.get_str_data())
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show:
            print(f'Графическое отображеные данных: {self.get_str_data()}')
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show:
            print(f"Столбчатая диаграмма: {self.get_str_data()}")
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))
# здесь создаются объекты классов и вызываются нужные методы
gr_1 = Graph(data_graph)

gr_1.show_bar()
gr_1.set_show(fl_show=False)
gr_1.show_table()
