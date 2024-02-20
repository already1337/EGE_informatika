def f(x): return #Функции x+1 и т.п.

stop_list = [] #Числа, которые нельзя
traectory = [] #Числа, которые надо
answer = 1


def g(x, y):
    if x == y: return 1
    if x > y or x in stop_list: return 0
    return sum(g(e, y) for e in f(x))


for i in range(len(traectory) - 1):
    answer *= g(traectory[i], traectory[i + 1])
print(answer)
