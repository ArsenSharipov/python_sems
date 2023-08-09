array = list()
n = int(input('Введите количество элеменитов массива: '))
print('Теперт заполните массив: ')
for i in range(n):
    array.append(int(input()))
print('Ваш масив: ', array)
max = int(input('Укажите верхнюю границу диапазона: '))
min = int(input('Укажите нижнюю границу диапазона: '))
for i in range(len(array)):
    if min < array[i] < max:
        print(array[i], end=' ')