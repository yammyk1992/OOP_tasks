# считывание строки и разбиение ее по пробелам
lst_in = input().split()


# hello 1 world -2 4.5 True
def check(x):
    try:
        int(x)
        return int(x)
    except ValueError:
        try:
            float(x)
            return float(x)
        except ValueError:
            return x


lst_out = map(check, [i for i in lst_in])
print(list(lst_out))