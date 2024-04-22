a = 'БАЛКОН'
c = 0
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    s = i + j + k + l + m
                    if s.count('Б') >= 2:
                        print(s)
                        c += 1
print(c)
