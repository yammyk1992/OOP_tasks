class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, a):
        if self.validate(a):
            self.__x = a

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, b):
        if self.validate(b):
            self.__y = b

    @staticmethod
    def norm2(vector):
        return (vector.x * vector.x) + (vector.y * vector.y)

    def validate(self, value):
        return isinstance(value, (int, float)) and self.MIN_COORD < value < self.MAX_COORD


v1 = RadiusVector2D()  # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)  # радиус-вектор с координатами (1; 0)
r5 = RadiusVector2D(10, 20)  # радиус-вектор с координатами (1; 2)
print(r5.norm2(r5))
