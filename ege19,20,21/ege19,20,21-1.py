def f(s,m):
  if s >= 129:
      return m % 2 == 0
  if m == 0:
    return 0
  if m % 2 != 0:
    return f(s+1, m-1) or f(s*2, m-1)
  else:
    return f(s+1, m-1) and f(s*2, m-1)

print('19)', *[s for s in range(1,129) if f(s,2)])
print('20)', *[s for s in range(1,129) if not f(s,1) and f(s,3)])
print('21)', *[s for s in range(1,129) if not f(s,2) and f(s,4)])

# P-02 (демо-2023). Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит
# куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один камень или увеличить количество камней в куче в два раза. Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней. Игра завершается в тот момент, когда количество камней в куче становится не менее 129. Победителем считается игрок, сделавший последний ход, т.е. первым получивший кучу, в которой будет 129 или больше камней.
# В начальный момент в куче было S камней, 1 ≤ S ≤ 128.
# Задание 19.
# Укажите такое значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть своим первым ходом.
#
# Задание 20.
# Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
# − Петя не может выиграть за один ход;
# − Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
# Найденные значения запишите в ответе в порядке возрастания.
# Задание 21
# Найдите значение S, при котором одновременно выполняются два условия:
# – у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
# – у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.