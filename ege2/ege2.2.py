print('w x y z')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((z <= w) or (y == w)) and ((x or z) == y) == True:
                    print(w, x, y, z)

# Логическая функция F задаётся выражением (x ∧ ¬y) ∨ (y ≡ z) ∨ w.
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.