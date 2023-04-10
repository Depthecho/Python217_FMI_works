# Преобразуйте матрицу(n, m) таким образом, чтобы строки с нечётными индексами были упорядочены по убыванию,
# а с чётными - по возрастанию:

import random

# Создание матрицы
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
matrix = [[random.randint(1, 20) for i in range(m)] for j in range(n)]
print("Исходная матрица:")
[print(*row, sep='\t') for row in matrix]

# Упорядочивание строк матрицы
for i in range(n):
    if i % 2 == 0:
        # Если индекс строки четный, сортируем по возрастанию
        matrix[i] = sorted(matrix[i])
    else:
        # Если индекс строки нечетный, сортируем по убыванию
        matrix[i] = sorted(matrix[i], reverse=True)

print("Преобразованная матрица:")
[print(*row, sep='\t') for row in matrix]
