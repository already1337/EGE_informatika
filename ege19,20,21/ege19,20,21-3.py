# число совершённых ходов prevMoves
# наибольшее возможное количество ходов moveWin
# Четыре параметра
def f( a, b, prevMoves, moveWin ):
    if a + b >= 77:
      return prevMoves % 2 == moveWin % 2
    if prevMoves == moveWin: return 0
    h = [ f(a+1, b, prevMoves+1, moveWin),
          f(a, b+1, prevMoves+1, moveWin),
          f(a*2, b, prevMoves+1, moveWin),
          f(a, b*2, prevMoves+1, moveWin)]
    return any(h) if (prevMoves+1) % 2 == moveWin % 2 else all(h)
# Если moveWin нечётное, то проверяется возможность победы первого игрока,
# для чётных победа второго игрока.
# При анализе следующих ходов мы исходим из принципа,
# что если их чётность совпадает с moveWin, то достаточно победы в одном из них.
# В противном случае победа должна быть во всех случаях
def f1( a, b, prevMoves, moveWin ):
    if a + b >= 77:
      return prevMoves % 2 == moveWin % 2
    if prevMoves == moveWin: return 0
    h = [ f(a+1, b, prevMoves+1, moveWin),
          f(a, b+1, prevMoves+1, moveWin),
          f(a*2, b, prevMoves+1, moveWin),
          f(a, b*2, prevMoves+1, moveWin)]
    return any(h)

#Для выполнения 19 задания создадим функцию f1 аналогичную f,
# кроме замены последней строки на return any(h)
# для поиска победы хотя бы при одном из ходов противника
# и найдём минимальное значение с выигрышной стратегией за 2 хода.

print('19)', min(s for s in range(1,70) if f1(7,s,0,2)))

# Для нахождения ответа на 20 задание найдём значения S,
# для которых не существует выигрышной стратегии за 1 ход,
# но существует за 3 хода.
print('20)', *[s for s in range(1,70)
    if not f(7,s,0,1) and f(7,s,0,3)])
# Для нахождения ответа на 21 задание найдём значение S,
# для которого не существует выигрышной стратегии за 2 хода,
# но существует за 4 хода.
print('21)', min(s for s in range(1,70)
    if not f(7,s,0,2) and f(7,s,0,4)))

# P-00 (демо-2021). Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежат две кучи камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в одну из куч (по своему выбору) один камень или увеличить количество камней в куче в два раза. Игра завершается в тот момент, когда суммарное количество камней в кучах становится не менее 77. Победителем считается игрок, сделавший последний ход, т.е. первым получивший такую позицию, при которой в кучах будет 77 или больше камней. В начальный момент в первой куче было семь камней, во второй куче – S камней; 1 ≤ S ≤ 69.
# Задание 19.
# Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите минимальное значение S, когда такая ситуация возможна.
#
# В задачах такого типа «неудачным» считается такой ход Пети, после которого
# 1)	он проиграет, хотя мог бы выиграть, ИЛИ...
# 2)	он проиграет быстрее (за меньшее число ходов) чем мог бы, если бы старался затянуть игру.
#
# Задание 20.
# Найдите два таких значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
# − Петя не может выиграть за один ход;
# − Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
# Найденные значения запишите в ответе в порядке возрастания.
# Задание 21
# Найдите минимальное значение S, при котором одновременно выполняются два условия:
# – у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
# – у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
