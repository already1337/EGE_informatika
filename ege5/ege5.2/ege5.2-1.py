for i in range(100, 1000):
    s = str(i)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    first = str(max(k1, k2))
    second = str((min(k1, k2)))
    s1 = first + second
    if s1 == '1412':
        print(i)
        break

# Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
# 1.Складываются первая и вторая, а также вторая и третья цифры исходного числа.
# 2.Полученные два числа записываются друг за другом в порядке убывания (без разделителей).
# Пример. Исходное число: 348. Суммы: 3 + 4 = 7; 4 + 8 = 12. Результат: 127. Укажите наименьшее число, в результате обработки которого автомат выдаст число 1412.