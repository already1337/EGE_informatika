a = set()
b = {2,4,6,8,10,12}
c = {3,6,9,12,15}

def f(x):
    A = x in a
    B = x in b
    C = x in c
    return B<=((C and (not A))<=(not B))

for x in range(1000):
    if f(x) == 0:
        a.add(x)
print(a)

# Элементами множеств А, P, Q являются натуральные числа, причём P={1,3,4,9,11,13,15,17,19,21}, Q={3,6,9,12,15,18,21,24,27,30}. Известно, что выражение
# ((x ∈ P) → (x ∈ A)) ∨ ((x ∉ A) → (x ∉ Q))
# истинно (т.е. принимает значение 1 при любом значении переменной х. Определите наименьшее возможное произведение элементов в множестве A.