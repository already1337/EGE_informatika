from ipaddress import *

net = ip_network('105.224.200.224/255.255.255.224')
k = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1') % 4 == 0:
        k += 1
print(k)

# Сеть задана IP-адресом 105.224.200.224 и сетевой маской 255.255.255.224.
# Сколько в этой сети IP-адресов, для которых
# количество единиц в двоичной записи IР-адреса кратно 4? В ответе укажите только число.