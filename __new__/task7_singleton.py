# здесь объявляйте класс SingletonFive
class SingletonFive:
    _instance = None
    _count = 0

    def __new__(cls, *args, **kwargs):
        if cls._count < 5:
            cls._instance = super().__new__(cls)
            cls._count += 1

        return cls._instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять
# print(id(objs[4]), id(objs[3]))


class Singleton:
    _instance = None
    count_obj = 0

    def __new__(cls, *args, **kwargs):
        if cls.count_obj < 999:
            cls._instance = super().__new__(cls)
            cls.count_obj += 1
        return cls._instance

    def __init__(self, name):
        self.name = name


obj = [Singleton("red") for i in range(6)]
for i in obj:
    print(id(i))
