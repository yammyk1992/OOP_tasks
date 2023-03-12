class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money:
    type_money = None
    EPS = 0.1

    def __init__(self, volume=0):
        # ссылка на класс CentralBank (центральный банк, изначально None);
        self.__cb = None
        # объем денежных средств в кошельке (если не указано, то 0).
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def get_volumes(self, other):
        if self.cb is None:
            raise ValueError("Неизвестен курс валют")

        if self.type_money is None:
            raise ValueError("Неизвестен тип кошелька")

        v1 = self.volume / self.cb.rates[self.type_money]
        v2 = other.volume / other.cb.rates[other.type_money]

        return v1, v2

    def __eq__(self, other):
        v1, v2 = self.get_volumes(other)
        return abs(v1 - v2) < self.EPS

    def __lt__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 < v2

    def __le__(self, other):
        v1, v2 = self.get_volumes(other)
        return v1 <= v2


class MoneyR(Money):
    type_money = "rub"


class MoneyD(Money):
    type_money = "dollar"


class MoneyE(Money):
    type_money = "euro"


rub = MoneyR()  # с нулевым балансом
dl = MoneyD(1501.25)  # с балансом в 1501.25 долларов
euro = MoneyE(100)  # с балансом в 100 евро

# rub < dl
# dl >= euro
# rub == euro  # значения сравниваются по текущему курсу центрального банка с погрешностью 0.1 (плюс-минус)
# euro > rub
r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
