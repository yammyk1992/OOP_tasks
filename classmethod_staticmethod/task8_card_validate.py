from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number):
        s = number.split("-")
        print(s)
        if len(number[4::5]) == 3:
            res = [i for i in number if i != "-"]
            if set(res) <= set(CardCheck.CHARS_FOR_NAME[-10::1]) and len(res) == 16:
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def check_name(cls, name):
        print(name.split())
        if name.count(" ") == 1:
            if set(name.replace(" ", "")) <= set(cls.CHARS_FOR_NAME):
                return True
            else:
                return False
        else:
            return False


is_number = CardCheck.check_card_number("1349-5678-9012-0000")
is_name = CardCheck.check_name("SERGEY BALAKIREV")
print(is_number)
print(is_name)
