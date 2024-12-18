print('Введите количество строк/столбцов')
a = int(input())

def com(n, k):
    if k == 0 :
        return 1
    if k == n:
        return 1
    return com(n - 1, k - 1) + com(n - 1, k)

# Увеличивается количество колон (строк) на один
def pascals_triangle_rows(rows):
    for i in range( rows):
        result = ""
        for colon in range( i + 1):
            result =result + str(com(i, colon)) + "\t"
        print(result)
        
print('pascals_triangle_rows(',a,')=')
pascals_triangle_rows(a)
# Количество строк/столбцов 