def input_int_numbers():
    try:
        return tuple(map(int, input().split()))
    except ValueError:
        raise TypeError('все числа должны быть целыми')


flag = True
while flag:
    try:
        tmp = input_int_numbers()
    except TypeError as err:
        continue
    else:
        flag = False
        print(*tmp)
