net_address = list(map(int, "111.81.192.0".split('.')))#Адрес сети
address = list(map(int,"111.81.208.27".split('.')))#IP
byte_n = 3
for i in range(256):
    if address[byte_n-1]&i == net_address[byte_n-1]:
        flag1 = False
        flag2 = True
        for x in f'{i:08b}':
            if x=='0': flag1 = True
            if flag1 and x=='1': flag2 = False
        if flag2:
            print(i)

# Для узла с IP-адресом 147.192.92.64 адрес сети равен 147.192.80.0.
# Чему равно значение третьего слева байта маски? Ответ запишите в виде десятичного числа.
