s = '8' * 1000
while ('999' in s) or ('888' in s):
    if '888' in s:
        s = s.replace('888', '9', 1)
    else:
        s = s.replace('999', '8', 1)
print(s)

s = '8' * 70
while '2222' in s or '8888' in s:
    if '2222' in s:
        s = s.replace('2222', '88', 1)
    else:
        s = s.replace('8888', '22', 1)
print(s)

s = '1' * 100
while '111' in s:
    s = s.replace('11', '2', 1)
    s = s.replace('22', '1', 1)
print(s)
