a = 'МАНОК'
a1 = 'МАНК'
c = 0
for i in a1:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    s = i + j + k + l + m
                    if (not 'АО' in s) and (s.count('М') == 1) and (s.count('А') == 1) and (s.count('Н') == 1) and (s.count('О') == 1) and (s.count('К') == 1):
                        print(s)
                        c += 1
print(c)
