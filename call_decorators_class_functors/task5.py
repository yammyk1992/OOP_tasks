class DigitRetrieve:
    def __call__(self, integer, *args, **kwargs):
        return is_number(integer)


def is_number(str):
    try:
        int(str)
        return int(str)
    except ValueError:
        return None


dg = DigitRetrieve()
# d1 = dg("123")  # 123 (целое число)
# print(d1)
# d2 = dg("45.54")  # None (не целое число)
# print(d2)
# d3 = dg("-56")  # -56 (целое число)
# print(d3)
# d4 = dg("12fg")  # None (не целое число)
# d5 = dg("abc")   # None (не целое число)
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)
