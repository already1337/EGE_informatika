a = 'АБВГДЯ'
a1 = 'АБВГД'
c = 0
for i in a:
    for j in a1:
        for k in a1:
            for l in a:
                s = i + j + k + l
                if s.count('Я') <= 1:
                    print(s)
                    c += 1
print(c)
