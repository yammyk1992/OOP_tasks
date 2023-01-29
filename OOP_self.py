# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f"Воспроизведение {self.filename}")
#
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
#
# media1.open("filemedia1")
# media2.open("filemedia2")
#
# media1.play()
# media2.play()

#
# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         lst = [str(i) for i in self.data if i in range(self.LIMIT_Y[0], self.LIMIT_Y[1]+1)]
#         return lst
#
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
#
# print(*graph_1.draw())
# здесь объявляется класс StreamData

# class StreamData:
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         else:
#             field = dict(zip(fields, lst_values))
#             for k, v in field.items():
#                 self.__setattr__(k, v)
#
#             return True if self.__dict__ == field else False
#
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = ["10", "Питон - основы мастерства", "512"]  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()


# # программу не менять, только добавить два метода
# lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']  # считывание списка строк из входного потока
#
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     # здесь добавлять методы
#     def select(self, a, b):
#         return self.lst_data[a: b + 1]
#
#     def insert(self, data):
#         for x in data:
#             self.lst_data.append(dict(zip(self.FIELDS, x.split())))
#
#
# db = DataBase()
# db.insert(lst_in)

class Translator:

    def add(self, eng, rus):

        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])

        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return list(self.tr.get(eng))


tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(*tr.translate("go"))
