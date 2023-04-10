# Дано целое число numRows, numColumns
# вернуть первые numRows ряды треугольника Паскаля.
# В треугольнике Паскаля каждое число является суммой 2 чисел, стоящих непосредственно над ним
#         [1]
#        [1][1]
#      [1][2][1]
#     [1][3][3][1]
#   [1][4][6][4][1]

numRows, numColumns, numRowsAnswer = int(input('Введите количество строк: ')), \
                                     int(input('Введите количество столбцов: ')), \
                                     int(input('Введите количество первых рядов, которые вы хотите вывести: ')) \

triangle = list()  # Создаем список треугольника

for i in range(numRows + 1):
    triangle.append([1] + [0] * numColumns)  # Заполняем список треугольника

for j in range(1, numRows + 1):
    for k in range(1, numColumns):
        triangle[j][k] = triangle[j - 1][k] + triangle[j - 1][k - 1]  # Создаём формулу для элемента в списке

for j in range(numRows - numRowsAnswer + 1, numRows + 1):  # Или же range(0, numRows+1) для вывода всего треугольника
    for k in range(0, numColumns):
        print(triangle[j][k], end="\t")
    print()  # Вывод треугольника
# Честно, не особо понял смысла задачи, сделал вот так
