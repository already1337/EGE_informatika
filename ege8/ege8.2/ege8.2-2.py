from itertools import product
words = list(product('ИОУ', repeat=5))
print(*words[239])

# Все 5-буквенные слова, составленные из букв И, О, У, записаны в алфавитном порядке и пронумерованы. Вот начало списка:
# 1.ИИИИИ
# 2.ИИИИО
# 3.ИИИИУ
# 4.ИИИОИ
# Запишите слово, которое стоит под номером 240.