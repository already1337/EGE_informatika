a1 = '1357'
a2 = '0246'
c = 432
for i in a1:
    for j in a2:
        for k in a1:
            for l in a2:
                for m in a1:
                    for n in a2:
                        s = i + j + k + l + m + n
                        if len(set(s)) == 6:
                            print(s)
                            c += 1
print(c)
