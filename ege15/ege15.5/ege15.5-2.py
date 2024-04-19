def f(x, y): return (2 * y + 3 * x < a) or (x + y > 40)

for a in range(1, 200):
    if all(f(x, y) == 1 for x in range(0, 150) for y in range(0, 150)):
        print(a)

# Укажите наименьшее целое значение А, при котором выражение
# (2y + 3x < A) or (x + y > 40)
# истинно для любых целых неотрицательных значений x и y.