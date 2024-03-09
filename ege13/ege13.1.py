mask = "255.255.255.224".split('.')#Маска
address = "162.198.0.157".split('.')#Адрес
number = ""
for i in range(len(mask)):
    bin_mask_i = f'{int(mask[i]):08b}'
    bin_address_i = f'{int(address[i]):08b}'
    for j in range(len(bin_mask_i)):
        if bin_mask_i[j] == '0':
            number += bin_address_i[j]
print(int(number, 2))

# Маской подсети называется 32-разрядное двоичное число, которое определяет, какая часть IP-адреса компьютера относится к адресу сети, а какая часть IP-адреса определяет адрес компьютера в подсети.
# В маске подсети старшие биты, отведенные в IP-адресе компьютера для адреса сети, имеют значение 1; младшие биты, отведенные в IP-адресе компьютера для адреса компьютера в подсети, имеют значение 0.
# Если маска подсети 255.255.255.224 и IP-адрес компьютера в сети 162.198.0.157, то порядковый номер компьютера в сети равен_____