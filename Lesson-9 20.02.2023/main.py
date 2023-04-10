# ДЗ
# 2.
# width = int(input('Введите ширину матрицы: '))
# height = int(input('Введите высоту матрицы: '))
# matrix = []
# for i in range(height):
#     matrix.append([])
#     for j in range(width):
#         matrix[i].append(i + j)
#
# for row in matrix:
#     for el in row:
#         print(el, end='\t')
#     print()
#
# 3.
# import random
# matrix = [[random.randint(0, 10) for i in range(5)] for j in range(5)]
#
# for row in matrix:
#     for el in row:
#         print(el, end='\t')
#     print()
#
# sums = []
# for i in range(len(matrix)):
#     sums.append([sum(matrix[i]), i])
#     summa = 0
#     for j in range(len(matrix[0])):
#         summa += matrix[j][i]
#     sums.append([summa, i + 5])
#
# sums.sort()
# print('-'*10)
# if sums[0][1] >= 5:
#     sums[0][1] -= 5
#     for i in range(len(matrix)):
#         print(matrix[i][sums[0][1]])
# else:
#     result = list(map(str, matrix[sums[0][1]]))
#     print('\t'.join(result))
#
# ----------------------------------------------


# 1.
#
# import random
#
# n = int(input('Введите размер матрицы: '))
# matrix = [[random.randint(1, 100) for i in range(n)] for j in range(n)]
#
# [print(*row, sep='\t') for row in matrix]
#
# 1 вариант нахождения минимума
# minimum = matrix[0][0]
# for i in range(n):
#     if minimum > matrix[i][i]:
#         minimum = matrix[i][i]
#
# 2 вариант нахождения минимума
# minimum = matrix[0][0]
# for i in range(n):
#     minimum = min(minimum, matrix[i][i])
#
# 3 вариант нахождения минимума
# minimum = min([matrix[i][i] for i in range(n)])
#
# print(minimum)


# 2.
#
# import random
# first = random.randint(0, 6)
#
# matrix = [['']*first]
#  # matrix = [[]]
# num_week = 0
# day = 1
# while day < 32:
#     if len(matrix[num_week]) < 7:
#         matrix[num_week].append(day)
#         day += 1
#     else:
#         num_week += 1
#         matrix.append([])
#
# [print(*row, sep='\t') for row in matrix]
#
# new_days = matrix.copy()
# for i in range(len(matrix)):
#     new_days[i] = matrix[i][:5]
#
# [print(*row, sep='\t') for row in new_days]


# 3.
# import random
#
# n, m = int(input('Введите ширину матрицы: ')), \
#        int(input('Введите высоту матрицы: '))
# matrix = [[random.randint(0, 4) for i in range(m)]
#                                 for j in range(n)]
#
# [print(*row, sep='\t') for row in matrix]
#
# res = 1
# for row in matrix:
#     for el in row:
#         res *= el if el != 0 else 1
#
# print(res)
#
#

# 4.
#
# import random
# n, m = int(input('Введите ширину матрицы: ')), \
#        int(input('Введите высоту матрицы: '))
# k = int(input('Введите число сдвигов: '))
# matrix = [[random.randint(1, 20) for i in range(n)]
#                                  for j in range(m)]
#
# [print(*row, sep='\t') for row in matrix]
#
# for _ in range(k):
#     first = matrix[0][0]
#     for i in range(m-1, -1, -1):
#         for j in range(n-1, -1, -1):
#             if i == m - 1 and j == n - 1:
#                 matrix[0][0] = matrix[i][j]
#             elif j == n - 1:
#                 matrix[i + 1][0] = matrix[i][j]
#             else:
#                 matrix[i][j + 1] = matrix[i][j]
#     matrix[0][1] = first
#
# print('-'*20)
# [print(*row, sep='\t') for row in matrix]

