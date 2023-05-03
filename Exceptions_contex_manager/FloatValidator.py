class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def check_value(self, value):
        if type(value) != float or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')
        return True

    def __call__(self, value, *args, **kwargs):
        if self.check_value(value):
            return value


class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value, *args, **kwargs):
        if type(value) != int or not (self.min_value <= value <= self.max_value):
            raise ValueError('значение не прошло валидацию')


def is_valid(lst, validators):
    res = []
    for i in lst:
        for x in validators:
            try:
                x(i)
                res.append(i)
                break
            except ValueError:
                pass
    return res


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
print(*lst_out)
# fv = FloatValidator(0, 6)
# fv(5.2)
# iv = IntegerValidator(1, 6)
# iv(4)
