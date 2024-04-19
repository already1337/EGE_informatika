for x in [k * 0.25 for k in range(-10000, 10000)]:
    A = 1
    P = 10 <= x <= 19
    Q = 25 <= x <= 35
    f = (A and not P) <= Q
    if f != 0:
        print(x)

# Наибольшее
