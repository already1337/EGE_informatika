from itertools import *

def f(x, y, z, w):
    return ((z <= w) or (y == w)) and ((x or z) == y)

for i in product([1, 0], repeat=4):
    t = ((0, 1, 1, 0), # первая
         (i[0], 1, 0, i[1]), # вторая
         (0, i[2], i[3], 1)) # третья
    if len(set(t)) == len(t): #если содержащий неповторяющиеся строки
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]: #[] - последний столбец таблицы по порядку
                print(*p)

# Логическая функция F задаётся выражением (x ∧ ¬y) ∨ (y ≡ z) ∨ w.
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.
