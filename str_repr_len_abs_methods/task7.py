from math import sqrt


class RadiusVector:
    def __init__(self, arg1, *args):
        if len(args) == 0:
            self.__radius = [0] * arg1
        else:
            self.__radius = [arg1] + list(args)

    def set_coords(self, *args):
        """для изменения координат радиус-вектора"""
        n = min(len(args), len(self.__radius))
        print(n, "NNNNNNN")
        self.__radius[:n] = args[:n]

    def get_coords(self):
        """для получения текущих координат радиус-вектора (в виде кортежа)"""
        return tuple(self.__radius)

    def __len__(self):
        """возвращает число координат радиус-вектора (его размерность)"""
        return len(self.__radius)

    def __abs__(self):
        return sqrt(sum([i * i for i in self.__radius]))


vector3D = RadiusVector(5)
vector3D.set_coords(3, -5.6, 8)
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D)  # res_len = 3
print(res_len)
res_abs = abs(vector3D)
print(res_abs)
