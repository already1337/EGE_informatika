def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

x = 4**2015 + 8**405 - 2**150 - 122
z = converter10_N(x, 2)
print(z.count('1'))

# Сколько единиц содержится в двоичной записи значения выражения: 4**2016 - 2**2018 + 8**800 - 80?