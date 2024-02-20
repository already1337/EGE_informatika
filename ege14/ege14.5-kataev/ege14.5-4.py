def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

a = "17"
b = "1700000"
summa = 0

while a <= b:
    summa += int(a, 8)
    a += "0"

answer = converter10_N(summa, 16)
print(answer)

# Найдите сумму восьмеричных чисел 17+170+1700+...+1700000, перевести в 16-ую систему счисления.
# Найдите в записи числа, равного этой сумме, третью цифру слева.
