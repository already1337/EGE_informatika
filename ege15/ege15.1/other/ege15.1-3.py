for x in [k * 0.25 for k in range(-10000, 10000)]:
    A = 0
    P = 13 <= x <= 27
    Q = 24 <= x <= 36
    f = P <= (Q and A)
    if f != 1:
        print(x)

# Наименьшее
