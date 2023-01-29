from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        TextInput.check_name(self.name)

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 50 >= len(name) >= 3:

            res = [True if i in TextInput.CHARS_CORRECT else False for i in name]
            if False in res:
                raise ValueError("некорректное поле name")
            else:
                return name
        else:
            raise ValueError("некорректное поле name")


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.name = name
        self.size = size
        PasswordInput.check_name(self.name)

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 50 >= len(name) >= 3:
            res = [True if i in PasswordInput.CHARS_CORRECT else False for i in name]
            if False in res:
                raise ValueError("некорректное поле name")
            else:
                return name
        else:
            raise ValueError("некорректное поле name")


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Лоalsjdkashudkhaksuhdkuahskudhakshdioasoidhiashdoiahsoidhaoishdoiahsiodhoiahsodi"), PasswordInput("Па"))
html = login.render_template()
