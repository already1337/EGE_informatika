p = [10, 40]  # Границы отрезока P в возврастающем порядке
q = [5, 15]  # Границы отрезока Q в возврастающем порядке
r = [35, 50]
points = p + q


def f(x, A):
    P = p[0] <= x <= p[1]
    Q = q[0] <= x <= q[1]
    R = r[0] <= x <= r[1]
    return (A or P) or (Q <= R)


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

# На числовой прямой даны три отрезка: P = [10, 40], Q = [5, 15] и R = [35, 50]. Какова наименьшая возможная длина промежутка A, что формула
# ( (x ∈ А) ∨ (x ∈ P) ) ∨ ((x ∈ Q)→ (x ∈ R))
# тождественно истинна, то есть принимает значение 1 при любом значении переменной х.