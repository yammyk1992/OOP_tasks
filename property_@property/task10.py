class PhoneBook:

    lst = []

    def add_phone(self, phone):
        self.lst.append(phone)

    def remove_phone(self, index):
        print(index)
        self.lst.pop(index)

    def get_phone_list(self):
        return self.lst


class PhoneNumber:

    def __init__(self, number, fio):
        if number == int and len(str(number)) == 11:
            self.number = number
        if fio == str:
            self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
p.remove_phone(0)
phones = p.get_phone_list()
print(phones)
