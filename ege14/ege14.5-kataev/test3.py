def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

for n in range(3, 100):
    z = 1 * n**2 + 2 * n + 1
    z7 = int('1532649855792092825102', 7)
    if z + 1 == z7:
        print(n)
        answer = converter10_N(n, 3)
        print(answer)
