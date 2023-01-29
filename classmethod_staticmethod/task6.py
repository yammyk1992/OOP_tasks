class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


class Factory:
    @classmethod
    def build_sequence(cls):
        return []

    @classmethod
    def build_number(cls, string):
        return int(string.replace('"', "").lstrip())


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)

