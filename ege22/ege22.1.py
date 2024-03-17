from csv import reader
with open("22.csv", encoding="cp1251") as F:
    rdr = reader(F, delimiter=';', quotechar='"')
    next(rdr) # читаем заголовки и пропускаем их
    data = {}
    finalTime = {}
    for s in rdr:
        id, t = int(s[0]), int(s[1])
        dependson = list(map(int, s[2].split(';')))
        print(id, t, dependson)
        if dependson == [0]:
            finalTime[id] = t # известно время окончания
        else:
            data[id] = (t, dependson)
print(finalTime)
print(data)
while data:
    ids = list(data.keys())
    for id in ids:
        t, dependson = data[id]
        if all((x in finalTime) for x in dependson):
            starlid = max(finalTime[x] for x in dependson)
            finalTime[id] = starlid + t
            del data[id]
print(finalTime)
print("Ответ:", max(finalTime.values()))