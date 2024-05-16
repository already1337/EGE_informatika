for x in '0123456789AB':
    for y in '0123456789AB':
        a = int(f'{x}231{y}', 12)
        b = int(f'78{x}98{y}', 14)
        if (a + b) % 99 == 0:
            print(a + b, (a + b) // 99)

# Операнды арифметического выражения записаны в системах счисления с основаниями 12 и 14:
# x231y12 + 78x98y14
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 99.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 99 и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.