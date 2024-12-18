print('Ввeдите числа, у которых будем искать НОД')
print('Ввод через Enter*')

a = int(input())
b = int(input())

# Делаем через остаток (в целом в этом заключается весь признак Евклида)
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)
    
# Выводим результат по примеру
result = gcd(a,b)
print ('gcd(',a,',',b,') =',result)
