# Объявите класс RandomPassword для генерации случайных паролей. Объекты этого класса должны создаваться командой:
#
# rnd = RandomPassword(psw_chars, min_length, max_length) где psw_chars - строка из разрешенных в пароле символов;
# min_length, max_length - минимальная и максимальная длина генерируемых паролей.
#
# Непосредственная генерация одного пароля должна выполняться командой:
#
# psw = rnd() где psw - ссылка на строку длиной в диапазоне [min_length; max_length] из случайно выбранных символов
# строки psw_chars.
#
# С помощью генератора списка (list comprehension) создайте список lst_pass из трех сгенерированных паролей объектом
# rnd класса RandomPassword, созданного с параметрами:
#
# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
# P.S. Выводить на экран ничего не нужно, только создать список из паролей.
#
# P.P.S. Дополнительное домашнее задание: попробуйте реализовать этот же функционал с использованием замыканий функций.
from random import randint


# class RandomPassword:
#     def __init__(self, psw_chars, min_length, max_length):
#         self.psw_chars = psw_chars
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, *args, **kwargs):
#         # print(args)
#         # return ''.join(self.psw_chars[i] for i in range(randint(self.min_length, self.max_length)))
#         return ''.join(self.psw_chars[i] for i in range(randint(self.min_length, self.max_length)))
#
#
# rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
# lst_pass = [rnd() for _ in range(3)]
# # one = rnd()
# # two = rnd()
# # three = rnd()
# # print([one, two, three])
# print(lst_pass)

class RandomPassword:
    def __init__(self, foo):
        self.foo = foo

    def __call__(self, chars, min=5, max=20, *args, **kwargs):
        return foo(chars, min, max)


def foo(chars, min, max):
    return ''.join(chars[i] for i in range(randint(min, max)))


rnd = RandomPassword(foo("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20))
print(*[rnd("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*") for _ in range(3)], sep=",")
