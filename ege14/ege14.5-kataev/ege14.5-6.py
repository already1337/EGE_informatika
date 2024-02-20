def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

for x in range(3, 31):
    z = converter10_N(x, 5)
    if z[0] == "3":  # if z[-2:] == "23":
        print(z, x)

# Укажите через запятую в порядке возрастания все десятичные числа, не превосходящие 30,
# запись которых в системе счисления с основанием 5 начинается на 3?