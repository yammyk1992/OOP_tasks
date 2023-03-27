class Bag:
    def __init__(self, max_weight):
        # максимальный суммарный вес предметов, который можно положить в сумку.
        self.max_weight = max_weight
        self.bags = []
        self.count = 0

    def check_count(self, new_t, old_t=None):
        w = self.count + new_t.weight if old_t is None else self.count + new_t.weight - old_t.weight
        if w > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing):
        """добавление нового объекта thing класса Thing в сумку."""
        self.check_count(thing)
        self.bags.append(thing)
        self.count += thing.weight

    def check_item(self, item):
        if item > len(self.bags):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.check_item(item)
        return self.bags[item]

    def __setitem__(self, key, value):
        self.check_item(key)
        t = self.bags[key]
        self.check_count(value, t)
        self.bags[key] = value
        self.count += (value.weight - t.weight)

    def __delitem__(self, key):
        self.check_item(key)
        t = self.bags.pop(key)
        self.count -= t.weight


class Thing:
    def __init__(self, name, weight):
        # название предмета (строка)
        self.name = name
        # вес предмета (вещественное или целочисленное значение)
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name)  # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name)  # платок
del bag[0]
print(bag[0].name)  # платок
t = bag[4]  # генерируется исключение IndexError
