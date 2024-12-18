print('Ввeдите числа, у которых будем искать НОД')
print('Ввод через Enter*')

a = int(input())
b = int(input())

# Делаем через остаток (в целом в этом заключается весь признак Евклида)
def gcd(a, b):
    while a!= 0 and b!= 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a or b

# Выводим результат по примеру
result = gcd(a,b)
print ('gcd(',a,',',b,') =',result)
