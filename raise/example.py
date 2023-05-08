class ExceptionPrint(Exception):
    """Общий класс исключения принтера"""


class ExceptionPrintSendData(ExceptionPrint):
    """Класс исключения при отправке данных принтеру"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Ошибка : {self.message}'


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать : {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('message')

    def send_to_print(self, data):
        return False


p = PrintData()
# p.print('123')
try:
    p.print('123')
except ExceptionPrintSendData as e:
    print(f'принтер не отвечает из except - {e} из send_data')
except ExceptionPrint:
    print("Общая ошибка печати")


# class LimitException(Exception):
#     """Превышение лимита"""
#
#
# error = LimitException('превышение лимита нагрузки')
# raise error

class LimitException(Exception):
    """Превышение лимита"""


class ServerLimitException(LimitException):
    """Превышение нагрузки на сервер"""


try:
    raise ServerLimitException('превышение серверной нагрузки')
except LimitException:
    print("LimitException")
except ServerLimitException:
    print("ServerLimitException")
