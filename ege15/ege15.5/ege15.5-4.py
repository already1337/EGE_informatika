for a in range(1, 1000):
    f = 0
    for x in range(1, 1001):
        for y in range(1, 1000):
            if ((x * y > a) and (x > y) and (x < 8)) == True:
                f = 1
                break
    if f == 0:
        print(a)
        break

# Для какого наименьшего целого числа A выражение
# (xy > A) ∧(x > y)∧(x < 8)
# тождественно ложно, т.е. принимает значение 0 при любых целых положительных x и y ?