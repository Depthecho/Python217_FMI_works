# 2.
# text = input('Введите текст: ')
# word1, word2, word3 = input('Введите 3 зарезервированные слова:\n'), \
#                       input(), input()
#
# text = text.replace(word1, word1.upper())
# text = text.replace(word2, word2.upper())
# text = text.replace(word3, word3.upper())
# print(text)

# 3.

# text = input('Введите текст: ')
# text = text.replace('...', '.')
# symboles = '!.?'
# count = 0
# for symbol in text:
#     if symbol in symboles:
#         count += 1
#
# print(count)

# --------------------------------

# import random
#
# random_nums = random.sample('abcdefg', 3)
# print(random_nums)

# row = [0] * 20
# matrix = [row] * 5

# print(matrix) - вывод таблицы в виде строки, что крайне неудобно

# for row in matrix:
#     print(*row)

# Конструкция для перебора ячеек матрицы
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(matrix[i][j])

# import random

# input() for x in range()
# matrix = [[random.randint(1, 20) for i in range(10)] for j in range(5)]

# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#     print()

# 1.
# width = int(input('Введите ширину матрицы: '))
# height = int(input('Введите высоту матрицы: '))
#                               столбец                 строка
# matrix = [[width * j + i + 1 for i in range(width)] for j in range(height)]

# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#     print()
# print()
# for i in range(height):
#     for j in range(width):
#         matrix[i][j] **= 2
#         print(matrix[i][j], end='\t')
#     print()


# 2.
# n, m = 10, 10
# matrix = [[0 for i in range(n)] for j in range(m)]
#
# for i in range(m):
#     for j in range(n):
#         if -1 <= i - j <= 1:
#             matrix[i][j] = 1
#
# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#     print()


# 3.

# import random
#
# n, m = 5, 5
# matrix = [[random.randint(1, 20) for i in range(n)] for j in range(m)]
#
# maximum = matrix[0][0]
# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#         if maximum < num:
#             maximum = num
#     print()
#
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == maximum:
#             print(j, end=' ')


# 4.

# import random
#
# n, m = 3, 2
# matrix = [[random.randint(1, 20) for i in range(n)] for j in range(m)]
#
# for row in matrix:
#     for num in row:
#         print(num, end='\t')
#     print()
#
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == min(matrix[i]):
#             minimum = True
#         else:
#             minimum = False
#
#         maximum = True
#         for k in range(m):
#             if matrix[i][j] < matrix[k][j]:
#                 maximum = False
#         if minimum and maximum:
#             print(matrix[i][j], end=' ')


