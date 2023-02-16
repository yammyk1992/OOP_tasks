# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, step=1, *args, **kwargs):
#         print("__CAAAAAAL__")
#         self.__counter += step
#         return self.__counter
#
#
# c = Counter()
# c2 = Counter()
# c(2)
# c()
# c()
# res = c()
# res2 = c2()
# print(res, res2)
# class StripChars:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         print(args)
#         if type(args[0]) != str:
#             # if not isinstance(args[0], str):
#             raise TypeError("Аргумент должен быть строкой!")
#
#         return args[0].strip(self.__chars)
#
#
# s = StripChars("?:!.;")
# res = s(" Hello World!!!")
# s2 = StripChars(" ")
# res2 = s2(" Hello World!!!")
# print(res, res2, sep='\n')
import math


class Derivate:
    def __init__(self, func):
        self.__fn = func

    # позволяет вызывать объекты класса подобно функциям, в котором определен метод __call__()
    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


# @Derivate
def df_sin(x):
    return math.sin(x)


# декоратор
df_sin = Derivate(df_sin)
print(df_sin(math.pi / 3))
