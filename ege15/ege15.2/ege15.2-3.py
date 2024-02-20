def Del(n, m):
    return n % m == 0

for A in range(1, 1000):
    A_podoshel = True
    for x in range(1, 1000):
        if ((Del(x, A) and Del(x, 45)) <= Del(x, 162)) and (A > 200) == True:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(A)

# (Не правльно написанная программа)