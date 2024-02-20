p = [5, 30]  # Границы отрезока P в возврастающем порядке
q = [14, 23]  # Границы отрезока Q в возврастающем порядке
points = p + q


def f(x, A):
    P = p[0] <= x <= p[1]
    Q = q[0] <= x <= q[1]
    return (P == Q) <= (not A)


answer = []
for a1 in points:
    for a2 in points:
        if a1 < a2:
            check = [[], [], [], []]
            for x in range(-10 ** 4, 10 ** 4):
                check[0].append(f(x, a1 <= x <= a2))
                check[1].append(f(x, a1 < x < a2))
                check[2].append(f(x, a1 < x <= a2))
                check[3].append(f(x, a1 <= x < a2))
            if any(all(i) for i in check):
                answer.append(abs(a2 - a1))

print(max(answer), min(answer))

# На числовой прямой даны два отрезка: P = [5, 30] и Q = [14, 23]. Укажите наибольшую возможную длину промежутка A, для которого формула
# ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.