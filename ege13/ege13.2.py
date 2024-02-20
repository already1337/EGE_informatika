mask = list(map(int, "255.255.192.0".split('.')))#Маска
address = list(map(int,"224.9.195.133".split('.')))#IP
print(*(mask[i]&address[i] for i in range(len(mask))))

# По заданным IP-адресу узла и маске определите адрес сети.
# IP –адрес узла: 224.9.195.133
# Маска: 255.255.192.0
