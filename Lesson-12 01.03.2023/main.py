# Домашнее задание

# 3.
# def draw_square(side, symbol, hollow):
#     if hollow:
#         for i in range(side):
#             for j in range(side):
#                 if i == 0 or i == side - 1 or j == 0 or j == side - 1:
#                     print(symbol, end=' ')
#                 else:
#                     print(' ', end=' ')
#             print()
#     else:
#         for i in range(side):
#             for j in range(side):
#                 print(symbol, end=' ')
#             print()
#
# draw_square(5, '*', False)

# 5.

# def mul(start, end):
#     result = 1
#     for i in range(min(start, end), max(start, end) + 1):
#         result *= i
#     return result
#
# print(mul(1, 5))


# Классная работа

# Игра "Крестики-нолики"

# board = [['_', '_', '_'],
#          ['_', '_', '_'],
#          ['_', '_', '_']]
#
#
# def check_win(board, symbol):
#     if ((board[0][0] == board[0][1] == board[0][2] == symbol) or
#         (board[1][0] == board[1][1] == board[1][2] == symbol) or
#         (board[2][0] == board[2][1] == board[2][2] == symbol) or
#         (board[0][0] == board[1][0] == board[2][0] == symbol) or
#         (board[0][1] == board[1][1] == board[2][1] == symbol) or
#         (board[0][2] == board[1][2] == board[2][2] == symbol) or
#         (board[0][0] == board[1][1] == board[2][2] == symbol) or
#         (board[0][2] == board[1][1] == board[2][0] == symbol)):
#         return True
#     return False
#
#
# def tic_tac_toe(turn=1):
#     [print(*row, sep=' ') for row in board]
#     symbol = 'X' if turn % 2 == 1 else 'O'
#     while True:
#         row = input('Введите номер строки(1-3): ')
#         col = input('Введите номер столбца(1-3): ')
#         if ((not row.isdigit() or not col.isdigit()) or
#            (row not in ['1', '2', '3'] or col not in ['1', '2', '3'])):
#             print('Неверный ввод!')
#         elif board[int(row) - 1][int(col) - 1] != '_':
#             print('Эта клетка уже занята!')
#         else:
#             row = int(row) - 1
#             col = int(col) - 1
#             break
#     board[row][col] = symbol
#     if check_win(board, symbol):
#         print(f'Победили {symbol}!')
#         [print(*row, sep=' ') for row in board]
#         return
#     elif turn == 9:
#         print(f'Ничья!')
#         [print(*row, sep=' ') for row in board]
#         return
#     tic_tac_toe(turn + 1)
#
# tic_tac_toe()

# Существует бесконечная возможность вложения функций внутри функций
# def foo():
#     def bar():
#         def ex():
#             print(1)
#         ex()
#     bar()
#
# foo()


# функция map()
# numbers = [1, 2, 3]
#
#
# def third_degree(n):
#     return n ** 3
#
#
# print(list(map(third_degree, numbers)))

# lambda функция/выражение
# lambda x: x + 1

# numbers = [1, 2, 3]
# print(list(map(lambda x: x ** 3, numbers)))

# c = (lambda x: print(x + 1))(4)
# print(c)

# Такой вариант использования не поддерживается
# add_one = lambda x: x + 1
#
# print(add_one(5))


# numbers = [1, 2, 3]
# str_list = lambda lst: [str(num) for num in lst]
# print(str_list(numbers))

# a, b = 2, 4
# print((lambda x, y: x + y)(a, b))


# 1.
# Напишите лямбда-функцию, которая принимает
# список целых чисел и возвращает новый список
# только с четными числами.

# nums = [1, 2, 3, 4, 5, 22]
# even_list = lambda lst: [num for num in lst if num % 2 == 0]
# print(even_list(nums))


# Пример передачи функции в качестве параметра в лямбду
# numbers = [1, 2, 3]
# func_list = lambda lst, func: [func(num) for num in lst]
# print(func_list(numbers, float))


# 2.
# Напишите лямбда-функцию, которая принимает
# список строк и возвращает новый список,
# содержащий только строки, содержащие букву «а».

# strings = ['abcxbsdg', 'gsdgdsb', '235tegdsxc']
# strings_with_a = lambda lst: [string for string in lst if 'a' in string]
# print(strings_with_a(strings))


# 3.
# Напишите лямбда-функцию, которая принимает
# список чисел и возвращает список чисел,
# являющихся идеальными квадратами.

# nums = [4, 16, 5, 9, 3, 1, 100]
# list_squares = lambda lst: [(num**0.5)**2 for num in lst]
# print(list_squares(nums))


# 4.
# Напишите лямбда-функцию, которая принимает
# список чисел и возвращает список чисел,
# которые больше среднего значения списка.

# nums = [1, 7, 9, 15, 2, 3, 0]
# higher_than_mean = lambda lst: [num for num in lst if num > sum(lst)/len(lst)]
# print(higher_than_mean(nums))


# Использование lambda-функции, как параметр внутри другой функции
# people = [['Egor', 180], ['Sasha', 178], ['Misha', 184], ['Katya', 181]]
# print(sorted(people, key=lambda lst: lst[1], reverse=True))


# 5.
# Напишите лямбда-функцию, которая принимает
# список строк и возвращает
# первую строку, содержащую цифру.

# strings = ['asfasg', 'asfas', '12asfa', 'asfas']
# first_string_with_digits = lambda lst: ([string for string in strings
#                                         if sum([char.isdigit() for char in string]) > 0] + ['Такой строки нет'])[0]
# print(first_string_with_digits(strings))


# 6.
# Напишите лямбда-функцию, которая принимает
# список списков [имя, балл] и возвращает
# имя учащегося с наивысшим баллом.

# students = [['Егор', 89], ['Ксюша', 80], ['Коля', 75], ['Маша', 91]]
# student_with_max_balls = lambda lst: sorted(lst, key=lambda x: x[1])[-1][0]
# print(student_with_max_balls(students))


