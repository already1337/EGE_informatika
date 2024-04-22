a = 'АВРОРА'
c = set()
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    for n in a:
                        s = i + j + k + l + m + n
                        t = [s.count(x) == a.count(x) for x in s]
                        if all(t) and (not 'РР' in s) and (not 'АА' in s):
                            c.add(s)
                            print(s)
print(len(c))
