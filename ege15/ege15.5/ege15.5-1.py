def f(x, y): return (y + 3 * x < a) or (x > 20) or (y > 40)

for a in range(1, 200):
    if all(f(x, y) == 1 for x in range(1, 150) for y in range(1, 150)):
        print(a)

# Укажите наименьшее целое значение А, при котором выражение
# (y + 3x < A) ∨ (x > 20) ∨ (y > 40)
# истинно для любых целых положительных значений x и y.