# Дан массив целых чисел
# Отсортируйте массив в порядкке возрастания в зависимости от частоты значений

# import random

# minimum = int(input('Введите минимальное число: '))
# maximum = int(input('Введите максимальное число: '))
# width = int(input('Введите ширину массива:'))

spisok = list(map(int, input('Введите целые числа: ').split()))
print(spisok)

sorted_spisok = list()

min_length_index = 0
while min_length_index != -1:
    min_length_index = -1
    for index, i in enumerate(spisok):
        i_length = spisok.count(i)
        m_length = spisok.count(spisok[min_length_index])
        if (min_length_index == -1 or m_length > i_length) and i not in sorted_spisok:
            min_length_index = index

    if min_length_index != -1:
        number = spisok[min_length_index]
        sorted_spisok.extend([number] * spisok.count(number))
print(sorted_spisok)
