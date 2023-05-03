# try:
#     f = open('myfile.txt')
# except FileNotFoundError:
#     print("Невозможно открыть файл")
#
# print('штатное завершение')

try:
    x, y, = map(int, input().split())
    res = x / y
except (ValueError, ZeroDivisionError):  # можно поймать просто AriphmeticException
    print('ошибка типа данных или деление на 0')
# except ZeroDivisionError:
#     print('деление на 0')

print('штатное завершение')

#                               BaseException
#                                    ^
#   _________________________________|____________________________________
#   ^                   ^                       ^                        ^
#   |                   |                       |                        |
# Exception        SystemExit             GeneratorExit       KeyboardInterrupt
#   ^
#   |
#   ----------------------------------------------------------------------
#   ^           ^         ^       ^        ^         ^         ^         ^
#   |           |         |       |        |         |         |         |
# Attribute  Arithmetic   EOF    Name    Lookup      OS       Type     Value
#  Error       Error     Error   Error    Error     Error     Error    Error
#               ^                          ^          ^
#               | - ZeroDivision           | - Index  | - FileNotFound
#               |    Error                 |   Error  |      Error
#               |                          |          |
#               | - FloatingPoint          | - Key    | - Interrupted
#               |      Error               |  Error   |      Error
#               |                                     |
#               | - Overflow Error                    | - Permission
#                                                     |      Error
#                                                     |
#                                                     | - TimeOut Error
