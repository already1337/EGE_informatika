for x in [k * 0.25 for k in range(-10000, 10000)]:
    A = 1
    P = 3 <= x <= 13
    Q = 12 <= x <= 22
    f = P <= (A <= P) or Q
    if f != 0:
        print(x)

# Наибольшее
