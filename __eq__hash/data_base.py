class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        """для добавления новой записи в БД, представленной объектом record;"""
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        """чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk (уникальное целое
        положительное число); запись ищется в значениях словаря (см. ниже) """
        r = (x for row in self.dict_db.values() for x in row)
        obj = tuple(filter(lambda x: x.pk == pk, r))
        return obj[0] if len(obj) > 0 else None


class Record:
    record_count = 0

    def __init__(self, fio, desc, old):
        self.fio = fio
        self.desc = desc
        self.old = old
        self.pk = self.__count()

    @classmethod
    def __count(cls):
        cls.record_count += 1
        return cls.record_count

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'Балакирев С.М.; преподаватель; 33'
          ]

db = DataBase("database.db")
for l in lst_in:
    args = list(map(str.strip, l.split(";")))
    args[-1] = int(args[-1])
    db.write(Record(*args))

