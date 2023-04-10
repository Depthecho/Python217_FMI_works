# print()
# input()
# sum()
# max()
# sorted()
# len()

# def - define/definition - определить/определение
# При именовании функций используется snake_case

# def hello():
#     print('Hello World!')
#
#
# hello()

# параметры
# def summa(a, b):
#     print(a + b)


# аргументы
# summa(2, 3)
# summa(4, 5)

# print(sum([1, 2, 3]))

# return - вернуться/вернуть
# def summa(a, b):
#     return a + b
#
#
# print(summa(2, 3))


# 1.
#
# def multiply(a, b):
#     return a * b
#
# def div(a, b):
#     if b == 0:
#         return 'Нельзя делить на ноль'
#     return a / b
#
# print(div(4, 0))

# ---------------
# print(print(6))
# None - ничего

# def summa(a, b):
#     print(a + b)
#     return
#
# print(summa(2, 3))
# ---------------

# 2.

# def get_odd_numbers_from(start, end):
#     if start > end:
#         print('Wrong values')
#     else:
#         [print(i, end=' ') for i in range(start, end) if i % 2 != 0]
#     print()
# get_odd_numbers_from(1, 15)
# get_odd_numbers_from(15, 1)

# 3.

# def draw_line(length, symbol, direction):
#     if direction == 'horizontal':
#         print(symbol*length)
#     elif direction == 'vertical':
#         [print(symbol) for i in range(length)]
#     else:
#         print('Wrong direction')
#
# draw_line(5, '8', 'right')


# def summa(a, b):
#     return a + b
#
# print(summa(a=3, b=2))


# Типы параметров и возвращаемого значения
# def summa(a: int, b: int) -> None:
#     return a + b
#
#
# print(summa(5, 4) + 5)

# print(5, end=' ')
# print(5)
# print(5)

# Параметры по умолчанию
# def summa(a: int = 0, b=0):
#     return a + b
#
#
# print(summa(True, 15))
# print(summa(5))
# print(summa())
# -------------------

# 4.

# def max_from_four(a: int, b: int,
#                   c: int, d: int):
#     maximum = a
#     for i in [b, c, d]:
#         if maximum < i:
#             maximum = i
#     return maximum
#
#
# print(max_from_four(4, 15, 7, 9))


# 5.

# def sum_range(start: int = 0, end: int = 10):
#     summa = 0
#     for i in range(min(start, end), max(start, end) + 1):
#         summa += i
#     return summa
#
#
# print(sum_range())


# 6.

# def is_prime(number: int) -> bool | str:
#     if number <= 1:
#         return 'Wrong number'
#     return not bool(sum([number % i == 0 for i in range(2, number // 2 + 1)]))
#
#
# print(is_prime(15))
