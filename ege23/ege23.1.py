def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x - 1, y) + f(x % 4, y)
print(f(45, 3))
