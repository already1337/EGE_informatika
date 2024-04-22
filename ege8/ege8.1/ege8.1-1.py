from itertools import *

k = 0
for x in product('КРОТ', repeat=6):
    s = ''.join(x)
    if s.count('О') == 1:
        k += 1
print(k)

# Вася составляет 6-буквенные слова, в которых есть только буквы К, Р, О, Т, причём буква О
# используется в каждом слове ровно 1 раз. Каждая из других допустимых букв может встречаться в
# слове любое количество раз или не встречаться совсем. Словом считается любая допустимая
# последовательность букв, не обязательно осмысленная. Сколько существует таких слов, которые
# может написать Вася?