from functools import *

@lru_cache(None)
def f(n):
    if n <= 7:
        return 1
    if n > 7:
        return n + 2 + f(n - 1)

for i in range(7, 2020):
    f(i)
print(f(2024) - f(2020))