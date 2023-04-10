# Домашнее задание

# 3
# def island_perimeter(matrix):
#     perimeter = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == 1:
#                 if j == 0 or matrix[i][j - 1] == 0:
#                     perimeter += 1
#                 if j == len(matrix[0]) - 1 or matrix[i][j + 1] == 0:
#                     perimeter += 1
#                 if i == 0 or matrix[i - 1][j] == 0:
#                     perimeter += 1
#                 if i == len(matrix) - 1 or matrix[i + 1][j] == 0:
#                     perimeter += 1
#
#     return perimeter
#
#
# map = [[0, 1, 1, 0],
#        [0, 1, 0, 0],
#        [0, 1, 1, 1],
#        [1, 1, 1, 0]]  # 5 + 4 + 5 + 4 = 18
# print(island_perimeter(map))

# 4.

# import random
#
# m, n = 4, 3
# matrix = [[random.randint(1, 10) for i in range(n)] for j in range(m)]
# [print(*row, sep='\t') for row in matrix]
# summa = 0
# while len(matrix[0]) > 0:
#     row_max = matrix[0][0]
#     for row in matrix:
#         row_max = max(row_max, max(row))
#         row.remove(max(row))
#     summa += row_max
# print(summa)


# def summa(a, b):
#
#     def check(a, b):
#         return a >= 0 and b >= 0
#
#     if check(a, b):
#         return a + b
#     else:
#         return check
#
#
# a = summa(4, -2)
# print(a(2, -2))


# Рекурсия в списках
# a = [1, 2, 3]
# a.append(a)
# print(a)
# print(a[3][3][3][3] == a[3])


# def fibo(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(40))

# Альтернатива range()
# def range(n, start=0):
#     if start < n:
#         print(start, end=' ')
#         range(n, start + 1)
#
# range(6)


# 1.

# def power(number, degree, base=1):
#     if degree == 0:
#         return base
#     print(base)
#     base *= number
#     return power(number, degree - 1, base)
#
# print(power(2, 5))


# 2.

# def summa(start, end, sum=0):
#     if start <= end:
#         return summa(start + 1, end, sum + start)
#     else:
#         return sum
#
#
# print(summa(1, 4))


# 3.

# def draw_line(n: int):
#     print('*', end='')
#     if n > 1:
#         draw_line(n - 1)
#
#
# draw_line(int(input('Введите число: ')))


# 4.

# def min_sum(numbers, i=0, index=0, minimum=0):
#     current_sum = sum([numbers[j] for j in range(i, i+10)])
#     if minimum > current_sum or minimum == 0:
#         minimum = current_sum
#         index = i
#     try:
#         return min_sum(numbers, i + 1, index, minimum)
#     except IndexError:
#         for i in range(len(numbers)):
#             if index <= i < index + 10:
#                 print('\033[32m', end='')
#             else:
#                 print('\033[0m', end='')
#             print(numbers[i], end=' ')
#         print()
#         return index, minimum
#
# import random
# nums = [random.randint(1, 20) for i in range(100)]
#
# print(min_sum(nums))
