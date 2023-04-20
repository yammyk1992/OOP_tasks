class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


# здесь объявляйте дочерние классы TemperatureView, PressureView и WetView

class TemperatureView(Observer):
    """слушатель для отображения информации о температуре"""

    def update(self, data):
        print(f"{self.__class__.__name__}: 'Текущая температура {data.temp}'")


class PressureView(Observer):
    """ слушатель для отображения информации о давлении;"""

    def update(self, data):
        print(f"{self.__class__.__name__}: 'Текущее давление {data.press}'")


class WetView(Observer):
    """ слушатель для отображения информации о влажности."""

    def update(self, data):
        print(f"{self.__class__.__name__}: 'Текущая влажность {data.wet}'")


subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

subject.change_data(Data(23, 150, 83))
# выведет строчки:
# Текущая температура 23
# Текущее давление 150
# Текущая влажность 83
subject.remove_observer(wet)
subject.change_data(Data(24, 148, 80))
# выведет строчки:
# Текущая температура 24
# Текущее давление 148
