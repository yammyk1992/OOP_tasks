class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    """для проверки длины данных в диапазоне [min_length; max_length];"""

    def __init__(self, min_lenght, max_lenght):
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght

    def __call__(self, string, *args, **kwargs):
        if self.max_lenght >= len(string) >= self.min_lenght:
            return True
        return False


class CharsValidator:
    """ для проверки допустимых символов в строке"""

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string, *args, **kwargs):
        if string in self.chars:
            return True
        else:
            return False


lv = LengthValidator(5, 20)  # min_length - минимально допустимая длина; max_length - максимально допустимая длина
cv = CharsValidator("chars")  # chars - строка из допустимых символов
# res = lv(string)
# res = cv(string)
