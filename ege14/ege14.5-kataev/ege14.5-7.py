def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

count = 0
for x in range(10, 18):
    z = converter10_N(x, 5)
    print(z)
    count += z.count("2")
print(count)

# Укажите, сколько всего раз встречается цифра 2 в записи чисел 10, 11, 12, 13, 14, 15, 16, 17
# в системе счисления с основанием 5.
