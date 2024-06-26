from itertools import *

def f(x):
    A = a1 <= x <= a2
    B = 24 <= x <= 90
    C = 47 <= x <= 115
    return C <= (((not A) and B) <= (not C))

Ox = [i/4 for i in range(20 * 4, 120 * 4)]
m = []
for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 1 for x in Ox):
        m.append(a2 - a1)
print(min(m))

# На числовой прямой даны два отрезка: В = [24; 90] и С= [47; 115]. Укажите наименьшую возможную длину такого.
# отрезка А, для которого логическое выражение:
# C <= (((not A) and B) <= (not C))
# истинно (т.е. принимает значение 1) при любом значении переменной х.