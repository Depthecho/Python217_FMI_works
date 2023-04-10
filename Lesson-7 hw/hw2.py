# Пользователь вводит размеры матрицы
# Напишите программу, которая заполнит матрицу по примеру ниже:
# Ввод: 4 и 3
# Вывод: 0123
#        1234
#        2345

rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

matrix = [[0 for j in range(columns)] for i in range(rows)]  # создаем матрицу, заполненную нулями

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = i + j  # заполняем матрицу значениями i+j

for row in matrix:
    print(" ".join(str(element) for element in row))
