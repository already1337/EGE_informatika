def converter_N_10(s, n):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ                                                                         '
    result = 0
    for i, digit in enumerate(reversed(s)):
        result += alpha.index(digit) * (n ** i)
    return result

def find_base():
    for base in range(2, 36):  # Перебираем основание системы счисления
        product = converter_N_10("12", base) * converter_N_10("31", base)
        if product == converter_N_10("402", base):
            return base
    return None

result = find_base()
print("Основание системы счисления:", result)

# В какой системе счисления выполняется равенство 12 X  * 31 X  = 402 X. В ответе укажите число – основание системы счисления.
