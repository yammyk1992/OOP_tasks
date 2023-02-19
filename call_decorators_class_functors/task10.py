class InputValues:
    def __init__(self, render):  # render - ссылка на функцию или объект для преобразования
        self.__render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func(*args, **kwargs).split()))
        return wrapper


class RenderDigit:
    def __call__(self, integer, *args, **kwargs):
        return is_number(integer)


def is_number(str):
    try:
        int(str)
        return int(str)
    except ValueError:
        return None


render = RenderDigit()
input_dg = InputValues(render)(input)
res = input_dg()
print(res)
# d1 = render("123")  # 123 (целое число)
# print(d1)
# d2 = render("45.54")
# print(d2)# None (не целое число)
# d3 = render("-56")   # -56 (целое число)
# print(d3)
# d4 = render("12fg")  # None (не целое число)
# d5 = render("abc")   # None (не целое число)
