class Integer:

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом!!!")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        # print(F"__set__: {self.name} = {value}")
        self.verify_coord(value)
        instance.__dict__[self.name] = value


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
