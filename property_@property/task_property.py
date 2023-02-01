class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def old(self):
        return self.__age

    @old.setter
    def old(self, age):
        self.__age = age

    @old.deleter
    def old(self):
        del self.__age


a = Person("Вася", "25")
a.old = 45
del a.old
print(a.__dict__)
