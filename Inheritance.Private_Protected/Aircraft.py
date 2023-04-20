class Aircraft:
    """самолет"""

    def __init__(self, model, mass, speed, top):
        self.check_str(model)
        self._model = model
        self.check_int(mass)
        self._mass = mass
        self.check_int(speed)
        self._speed = speed
        self.check_int(top)
        self._top = top

    def check_str(self, st):
        if type(st) != str:
            raise TypeError('неверный тип аргумента')

    def check_int(self, value):
        if type(value) not in (int, float) or value < 0:
            raise TypeError('неверный тип аргумента')

    def check_dict(self, d):
        if type(d) != dict:
            raise TypeError('неверный тип аргумента')

    def check_value(self, value):
        if type(value) != int or value < 0:
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    """пассажирский самолет"""
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self.check_value(chairs)
        self._chairs = chairs


class WarPlane(Aircraft):
    """военный самолет"""
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self.check_dict(weapons)
        self._weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
