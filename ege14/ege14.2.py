for x in '0123456789ABCDEF':
    t = int('2' + x + '84', 19) + int('2B3' + x + '', 16)
    if t % 88 == 0:
        print(x, t // 88)

# Операнды арифметического выражения записаны в системе счисления с основаниями 19 и 16:
# 2x8419 + 2B3x16
# В записи чисел переменной x обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 88.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 88 и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
