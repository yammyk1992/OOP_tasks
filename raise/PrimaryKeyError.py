class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if 'id' not in kwargs and 'pk' not in kwargs:
            self.message = "Первичный ключ должен быть целым неотрицательным числом"
        else:
            key, value = tuple(kwargs.items())[0]
            self.message = f"Значение первичного ключа {key} = {value} недопустимо"

    def __str__(self):
        return self.message


e1 = PrimaryKeyError()  # Первичный ключ должен быть целым неотрицательным числом
print(e1)
e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
print(e2)
e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
print(e3)
try:
    raise PrimaryKeyError(id=-10)
except PrimaryKeyError as p:
    print(p)
