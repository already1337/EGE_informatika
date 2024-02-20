def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

for n in range(2, 100):
    z = converter10_N(30, n)            # n - система счисления
    if len(z) == 3:
        print(z, n)

# Укажите наименьшее основание системы счисления, в которой запись числа 30 трёхзначна.
