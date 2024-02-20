count = 0
def F( n ):
    global count # если не объявить count глобальной – ошибка!
    print('*')
    count += 1
    if n >= 1:
        print('*')
        count += 1
        F(n-1)
        F(n//2)
F(140)
print(count)

# Определите, сколько символов * выведет эта процедура при вызове F(140):