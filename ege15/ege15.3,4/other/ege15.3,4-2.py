for A in range(1, 101):
    k = 0
    for x in range(1, 1000):
        if ((x & 28 != 0) or (x & 45 != 0)) <= ((x & 48 == 0) <= (x & A != 0)):
            k += 1
    if k == 999:
        print(A)
        break

# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наименьшего натурального числа А формула
# ДЕЛ(A, 45) ∧ (ДЕЛ(750, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(120, x)))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?



# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14 & 5 = 11102 & 01012 = 01002 = 4. Для какого наименьшего неотрицательного целого числа А формула
# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной x)?