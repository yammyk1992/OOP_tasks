class Clock:

    def __init__(self, time):
        if self.__check_time(time):
            self.__time = time
        else:
            raise ValueError("НЕДОПУСТИМОЕ ЗНАЧЕНИЕ")

    def set_time(self, tm):
        """публичный метод set_time(tm) для установки текущего времени (присваивает значение tm приватному локальному
         свойству time, если метод check_time(tm) возвратил True);"""
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        """публичный метод get_time() для получения текущего времени из приватной локальной переменной time"""
        return self.__time

    def __check_time(self, tm):
        """ приватный метод класса check_time(tm) для проверки корректности времени в переменной tm (возвращает True,
        если значение корректно и False - в противном случае)."""
        if type(tm) in (int, float) and 100_000 >= tm >= 0:
            return True
        else:
            return False


clock = Clock(4530)
print(clock)
