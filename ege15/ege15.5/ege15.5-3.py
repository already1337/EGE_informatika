k = 0
for x in range(0, 100):
    for y in range(0, 100):
        f = not(((x > 6) and (x + y >= 5)) or (y >= 5))
        if f == 1:
            k += 1
print(k)

# Сколько существует различных комбинаций неотрицательных целых значений x и y, при которых истинно выражение:
# not(((x > 6) and (x + y >= 5)) or (y >= 5))