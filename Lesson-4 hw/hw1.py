# Напишите программу, которая запрашивает два целых числа x и y, после чего вычисляет и выводит значение x в степени y.
x, y=int(input('Введите значение х: ')), int(input('Введите значение y: '))
for i in range(y):
    print(f'{x}^{i}={x**i}')