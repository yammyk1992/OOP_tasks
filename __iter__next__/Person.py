# class Person:
#     def __init__(self, fio, job, old, salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
#         self.person = [self.fio, self.job, self.old, self.salary, self.year_job]
#
#     def _check_index(self, value):
#         if value not in range(0, 5):
#             raise IndexError('неверный индекс')
#         return value
#
#     def __getitem__(self, item):
#         self._check_index(item)
#         return self.person[item]
#
#     def __setitem__(self, key, value):
#         self._check_index(key)
#         self.person[key] = value
#
#
# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123 # IndexError

# variant with __next__ and __iter__

class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._attrs = tuple(self.__dict__)
        self._len_attrs = len(self._attrs)
        self._iter_index = -1

    def _check_index(self, value):
        if not (-self._len_attrs <= value < self._len_attrs):
            raise IndexError('неверный индекс')
        return value

    def __getitem__(self, item):
        self._check_index(item)
        return getattr(self, self._attrs[item])

    def __setitem__(self, key, value):
        self._check_index(key)
        setattr(self, self._attrs[key], value)
        self.__dict__[key] = value

    def __iter__(self):
        self._iter_index = -1
        return self

    def __next__(self):
        if self._iter_index < self._len_attrs - 1:
            self._iter_index += 1
            return getattr(self, self._attrs[self._iter_index])
        raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
# pers[5] = 123 # IndexError
