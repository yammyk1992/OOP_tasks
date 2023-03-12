class Box:
    def __init__(self):
        self.boxes = []

    def add_thing(self, obj):
        self.boxes.append(obj)

    def get_things(self):
        return self.boxes

    def __eq__(self, other):
        if len(self.boxes) == len(other.boxes):
            name = [i.name for i in self.boxes]
            other_name = [i.name for i in other.boxes]
            mass = [i.mass for i in self.boxes]
            other_mass = [i.mass for i in other.boxes]

            return sorted(name) == sorted(other_name) and sorted(mass) == sorted(other_mass)

            # return all(i in other.get_things() for i in self.get_things())


class Thing:
    def __init__(self, name: str, mass: (int, float)):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


obj1 = Thing("name", 200)
obj2 = Thing("name2", 300)

b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2  # True
print(res)
