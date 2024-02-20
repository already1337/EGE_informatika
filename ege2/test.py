from itertools import *

def f(x, y, z):
    return (x == z) or (x <= (y and z))

for i in product([1, 0], repeat=3):
    t = ((0, 0, i[0]), # первая
         (1, i[1], i[2])) # третья
    if len(set(t)) == len(t): #если содержащий неповторяющиеся строки
        for p in permutations('xyz'):
            if [f(**dict(zip(p, r))) for r in t] == [0, 0]: #[] - последний столбец таблицы по порядку
                print(*p)
