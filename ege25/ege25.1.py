from fnmatch import *

for x in range(0, 10**10, 2024):
    if fnmatch(str(x), '1*2322?2'):
        print(x, x // 2024)

# Назовём маской числа последовательность цифр, в которой также
# могут встречаться следующие символы:
# 1) символ «?» означает ровно одну произвольную цифру;
# 2) символ «*» означает любую последовательность цифр
# произвольной длины; в том числе «*» может задавать и
# пустую последовательность.
# Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
# Среди натуральных чисел, не превышающих 10'°, найдите все числа,
# соответствующие маске 1*2322?2, делящиеся на 2024 без остатка.
# В ответе запишите в первом столбце таблицы все найденные числа в
# порядке возрастания, а во втором столбце — соответствующие им
# результаты деления этих чисел на 2024.
# Количество строк в таблице для ответа избыточно.