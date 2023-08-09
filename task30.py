def fill(a):
    A = list()
    first = int(input('Введите первый элемент: '))
    difference = int(input('Введите разность: '))
    for i in range(1, a+1):
        A.append(first + (i-1)*difference)
    return(A)    

n = int(input('Введите кол-во элем-ов прогрессии: '))
N = fill(n)
print(N)