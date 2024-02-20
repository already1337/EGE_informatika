def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

for x in range(6, 100):
    for y in range(6, 100):
        if (2 * x**2 + 2 * x + 5 == 4 * y**2 + 0 + 5):
            print(x, y)

# Чему равно наименьшее основание позиционной системы счисления, при котором 225x = 405y?
# Ответ записать в виде целого числа.
