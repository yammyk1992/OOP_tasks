# class Point:
#     def __init__(self, x, y, color="black"):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# points = [Point(2 * i + 1, 2 * i + 1) for i in range(0, 1000)]
# points[1].color = "yellow"
# from random import randint
#
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# elements = [(Line, Rect, Ellipse)[randint(0, 2)](1, 2, 3, 4) for n in range(217)]
# for obj in elements:
#     if isinstance(obj, Line):
#         obj.sp = (0, 0)
#         obj.ep = (0, 0)

# здесь объявите класс TriangleChecker
class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):

        if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
            return 1
        if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
            return 1

        self.a = a
        self.b = b
        self.c = c
        if a >= (b + c) or b >= (a + c) or c >= (a + b):
            return 2

        return 3


a, b, c = input().split()  # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
