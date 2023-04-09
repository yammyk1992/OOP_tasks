class Validator:
    def __call__(self, data):
        print(self, "SELLLLF")
        if not self._is_valid(data):
            raise ValueError('данные не прошли валидацию')
        return self._is_valid(data)

    def _is_valid(self, data):
        pass

    def __str__(self):
        return self.__class__.__name__


class IntegerValidator(Validator):  # для проверки, что data - целое число в заданном диапазоне
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        print("Вызвался у инта")
        return isinstance(data, int) and self.min_value <= data <= self.max_value


class FloatValidator(Validator):  # для проверки, что data - вещественное число в заданном диапазоне
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        return isinstance(data, float) and self.min_value <= data <= self.max_value


integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)
# res2 = float_validator(10)
print(res1)
