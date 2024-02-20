def f(x, A):
    return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))

print(min(A for A in range(0, 1000) if all(f(x, A) == 1 for x in range(0, 1000))))