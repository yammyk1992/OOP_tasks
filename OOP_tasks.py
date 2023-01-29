class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

    def get_bla(self, *args, **kwargs):
        a = args
        b = kwargs
        c = self

        print("HELLO")
        print(a)
        print(b)
        print(c)


p1 = Person()
print(True if p1.__dict__.get("job") else False)
p1.get_bla({"2": "asd"})

Person.get_bla(p1)
