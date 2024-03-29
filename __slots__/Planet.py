class Planet:
    def __init__(self, name, diametr, period_solar, period):
        # наименование планеты
        self._name = name
        # диаметр планеты (любое положительное число)
        self._diametr = diametr
        # период (время) обращения планеты вокруг Солнца (любое положительное число)
        self._period_solar = period_solar
        # период обращения планеты вокруг своей оси (любое положительное число).
        self._period = period


class SolarSystem:
    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


s_system = SolarSystem()

