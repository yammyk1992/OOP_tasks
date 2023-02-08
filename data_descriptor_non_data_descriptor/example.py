class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом!!!")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        print("Сработал геттер")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print("Сработал сеттер")
        # print(F"__set__: {self.name} = {value}")
        self.verify_coord(value)
        instance.__dict__[self.name] = value

    # def __del__(self):
    #     print("Сработал делитер")


class Point3d:
    a = Integer()
    b = Integer()
    z = Integer()

    def __init__(self, a, b, z):
        self.a = a
        self.b = b
        self.z = z


p = Point3d(1, 2, 3)
print(p.__dict__)
p.z = 6
print(p.__dict__)


class RealValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class StringField:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class DataBase:
    x = StringField()
    y = StringField()

    def __init__(self, x, y):
        self.x = x
        self.y = y


db = DataBase('hi', 'low')
db.__dict__['x'] = 'top'
print(db.x)
print(db.__dict__)
