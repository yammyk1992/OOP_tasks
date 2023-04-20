# class Geom:
#     name = 'Geom'
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f'инициализатор GEOM для {self.__class__}')
#         self._x1 = x1
#         self._y1 = y1
#         self._x2 = x2
#         self._y2 = y2
#
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         # super. возвращает объект поэтому нам ненадо писать в аргументах self
#         super().__init__(x1, y1, x2, y2)
#         print('инициализатор Rect')
#         self._fill = fill
#
#     def get_coords(self):
#         print(self.__class__)
#         return self._x1, self._y1
#
#
# g = Geom(1, 2, 3, 4)
#
# r = Rect(1, 2, 3, 4)
# print(r.get_coords())

# class Phone:
#     def __init__(self, model):
#         self.__model = model
#
#
# class SmartPhone(Phone):
#     def __init__(self, model, memory):
#         super().__init__(model)
#         self.__memory = memory
#
#     def get_info(self):
#         return self.__model, self.__memory
#
#
# phone = SmartPhone('iPhone 123', 1024)
# print(phone.__dict__)
# print(phone.get_info())

class Auto:
    __MIN_WEIGHT = 100
    __MAX_WEIGHT = 1000

    def __init__(self, model):
        self.__verify_model(model)
        self.__model = model

    def __verify_model(self, model):
        if type(model) != str:
            raise TypeError('модель должна представляться строкой')

    def __verify_weight(self, weight):
        if self.__MIN_WEIGHT > weight or weight > self.__MAX_WEIGHT:
            raise TypeError(f'вес автомобиля BMW должен быть в пределах [{self.__MIN_WEIGHT}; {self.__MAX_WEIGHT}]')


class BMW(Auto):
    def __init__(self, model, weight):
        super().__init__(model)
        self.__verify_weight(weight)
        self.__weight = weight


bmw_x5 = BMW('BMW X5', 512.5)
print(bmw_x5._BMW__weight)
print(bmw_x5._Auto__model)
