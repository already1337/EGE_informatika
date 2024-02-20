f = [0] * 2000
f[0] = 0
for n in range(1, 1001):
    if n % 2 == 0: f[n] = f[n // 2]
    if n % 2 != 0: f[n] = 1 + f[n - 1]
k = 0
for n in range(1, 1001):
    if f[n] == 3: k += 1
print(k)

# Алгоритм вычисления значения функции F(n), где n — целое неотрицательное число, задан следующими соотношениями:
# F(0) = 0;
# F(n) = F(n / 2), если n > 0 и при этом чётно;
# F(n) = 1 + F(n − 1), если n нечётно.
# Сколько существует таких чисел n, что 1 ≤ n ≤ 1000 и F(n) = 3?