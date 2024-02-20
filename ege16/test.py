def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 5 * f(n - 1) + 3 * n

print(f(4))
