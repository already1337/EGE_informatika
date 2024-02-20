def f(n):
    return G(n - 1)
def G(n):
    if n < 10:
        return n
    else:
        return G(n - 2) + 1

count = 0
for n in range(1, 101):
    result = f(n)
    sq = int(result**0.5)
    if sq > 0 and sq ** 2 == result:
        print(sq, result)
        count += 1

print(count)

# Алгоритм вычисления значений функций F(n) и G(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = G(n - 1),
# G(n) = n, если n < 10,
# G(n) =G(n – 2) + 1, если n >= 10
# Определите количество значений n на отрезке [1, 100],
# для которых значение функции F(n) будет полным квадратом некотого натурального числа.