def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

for n in range(2, 64):
    a = converter10_N(30, n)
    if a[-1] == "0" and len(a) == 4:
        print(n, a)

# Запись числа 30 в системе счисления с основанием N оканчивается на 0 и содержит 4 цифры.
# Чему равно основание этой системы счисления N?