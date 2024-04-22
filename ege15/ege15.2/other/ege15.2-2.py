def f(x, P, Q, A):
    return not(x in A) <= (not((x in P) or (x in Q)))

P = set([x for x in range(2, 21, 2)])
Q = set([x for x in range(3, 31, 3)])
A = set()
for x in range(60):
    if not f(x, P, Q, A):
        A.add(x)
print(len(A))

# Элементами множеств А, P, Q являются натуральные числа, причём
# P={2,4,6,8,10,12,14,16,18,20}, Q={3,6,9,12,15,18,21,24,27,30}.
# Известно, что выражение истинно (т.е. принимает значение 1 при любом значении переменной х.
# Определите наименьшее возможное количество элементов в множестве A.