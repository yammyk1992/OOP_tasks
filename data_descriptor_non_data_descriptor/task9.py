class Bag:
    def __init__(self, max_wieght):
        self.max_wieght = max_wieght
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if self.max_wieght > thing.weight:
            self.__things.append(thing)

    def remove_thing(self, index):
        self.__things.pop(index)

    def get_total_weight(self):
        x = [i.weight for i in self.__things]
        return sum(x)


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
print(w)
for t in bag.things:
    print(f"{t.name}: {t.weight}")
