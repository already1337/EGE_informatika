def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

for n in range(4, 100):
    z = converter10_N(94, n)
    if z[:2] == "23":  # if z[-2:] == "23":
        print(z, n)

# Укажите через запятую в порядке возрастания все основания систем счисления,
# в которых запись числа 94 начинается на 23.