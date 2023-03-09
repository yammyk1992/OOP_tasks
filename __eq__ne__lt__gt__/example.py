# __eq__ - equal to - равно
# __ne__ - not equal to - не равно
# __gt__ - greater than - больше, чем
# __ge__ - greater than or equal to - больше или равно
# __lt__ - less than - меньше, чем
# __le__ - less than or equal to - меньше или равно

class Clock:
    __DAY = 86400  # секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("seconds must be integer")
        self.seconds = seconds % self.__DAY

    @classmethod
    def validator_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("the right operand must be type int or object Clock")
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.validator_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.validator_data(other)
        return self.seconds < sc

    def __gt__(self, other):
        sc = self.validator_data(other)
        return self.seconds > sc

    def __ge__(self, other):
        sc = self.validator_data(other)
        return self.seconds <= sc


c1 = Clock(1500)
c2 = Clock(1900)
print(c1 != c2)
print(c1 > c2)
