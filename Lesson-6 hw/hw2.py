# В списке целых, заполненном случайными числами, определить минимальный и максимальный элементы, посчитать количество
# отрицательных элементов, посчи-тать количество положительных элементов, посчитать количество нулей. Результаты
# вывести на экран.

import random
spisok = [random.randint(-100, 100) for i in range(10)]
print(spisok)
i = 0
more_zero = 0
less_zero = 0
zero = 0
while i<len(spisok):
    symb_of_spisok = spisok[i]
    if symb_of_spisok > 0:
        more_zero += 1
    elif symb_of_spisok < 0:
        less_zero += 1
    else:
        zero += 1
    i += 1
print(f'Минимальное число списка: {min(spisok)}')
print(f'Максимальное число списка: {max(spisok)}')
print(f'Количество отрицательных чисел списка: {less_zero}')
print(f'Количество положительных чисел списка: {more_zero}')
print(f'Количство нулей в списке: {zero}')

