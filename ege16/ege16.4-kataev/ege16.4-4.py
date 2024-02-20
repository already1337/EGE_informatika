def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * G(n - 1) + 5 * n
def G(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + 2 * n

count = 0
for n in range(1, 101):
    result = f(n)
    sq = int(result ** 0.5)
    if sq > 0 and sq ** 2 == result:
        print(sq, result)
        count += 1

print(count)

# Определите количество значений n на отрезке [1, 100],
# для которых значение функции F(n) будет полным квадратом некоторго натурального числа.
