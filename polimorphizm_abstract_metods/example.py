# делаем имитацию абстрактного класса 
class Geom:
    def get_pr(self):
        raise NotImplementedError(f"Нет такого метода 'get_pr' в классе {self.__class__.__name__}")


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    # для реализации полиморфизма мы называем метод во всех классах одинаково и в разных классах переопределяем его
    # def get_pr(self):
    #     return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    # для реализации полиморфизма мы называем метод во всех классах одинаково и в разных классах переопределяем его
    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # для реализации полиморфизма мы называем метод во всех классах одинаково и в разных классах переопределяем его
    def get_pr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

geom = [r1, r2, s1, s2, t1, t2]
for g in geom:
    # if isinstance(g, Rectangle):
    #     print(g.get_pr())
    # else:
    #     print(g.get_sq_pr())
    print(g.get_pr())
