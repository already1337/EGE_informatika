from itertools import *
k = 0
for x in product('АПРСУ', repeat=5):
    s = ''.join(x)
    k += 1
    if s.count('У') <= 1 and 'АА' not in s:
        print(k, s)
        break

# Все 5-буквенные слова, в составе которых могут быть только буквы П, А, Р, У, С, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# ...
# Под каким номером в списке идёт первое слово, которое содержит не более одной буквы У и не содержит букв А, стоящих рядом.