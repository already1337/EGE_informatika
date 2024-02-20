def converter10_N(z, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    st = ''
    while z != 0:
        index = z % n
        st = alpha[index] + st
        z = z // n
    return st

count = 0

for x in range(2, 1000):  # Увеличил диапазон для более полного решения
    a1 = converter10_N(x, 16)
    a2 = converter10_N(x, 8)

    # Проверяем условие
    if '1' in a1 and '1' in a2 and a1.count('*') + a2.count('*') == 2:
        print(x, a1, a2)
        count += 1

print("Количество чисел:", count)

# Некоторое число X из десятичной системы счисления перевели в системы счисления с основаниями 16, 8.
# Часть символов при записи утеряна. Позиции утерянных символов обозначены символом *:
# X = 3*9 16 = 1** 8 .
# Сколько чисел соответствуют условию задачи?

