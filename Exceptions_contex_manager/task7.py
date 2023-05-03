lst_in = input().split()


def check(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


print(sum(map(int, filter(lambda x: check(x), lst_in))))
