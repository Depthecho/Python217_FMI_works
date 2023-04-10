# dictionary = {'Hello': 'Salut'}
#
# while True:
#     command = input('1. Добавить новое слово и перевод\n'
#                     '2. Удалить существующее слово и перевод\n'
#                     '3. Найти перевод слова на английском\n'
#                     '4. Изменить перевод существующего слова\n'
#                     'Введите команду: ')
#     if command == '1' or command == '4':
#         word = input('Введите слово на английском: ')
#         translation = input('Введите его перевод на французский: ')
#         dictionary[word] = translation
#         if command == '1':
#             print(f'Слово {word} и его перевод {translation} успешно добавлены!')
#         else:
#             print(f'Перевод слова {word} успешно изменён!')
#     elif command == '2':
#         word = input('Введите слово на английском: ')
#         del dictionary[word]
#         print(f'Слово {word} удалено!')
#     elif command == '3':
#         word = input('Введите слово на английском: ')
#         if word in dictionary:
#             print(f'Слово {word} на французский язык переводится, как:\n'
#                   f'{dictionary[word]}')
#         else:
#             print('Такого слова в словаре нет!')
#     else:
#         print('Такой команды нет! Завершаю работу...')
#         break
import time


# 3. Фирма
# dictionary = {}
# keys = ['phone', 'email', 'position', 'auditory', 'skype']
#
# while True:
#     command = input('1. Добавить нового сотрудника\n'
#                     '2. Удалить сотрудника\n'
#                     '3. Найти данные о сотруднике\n'
#                     '4. Изменить данные о сотруднике\n'
#                     'Введите команду: ')
#     if command == '1' or command == '4':
#         fio = input('Введите ФИО сотрудника через пробел: ')
#         if command == '4' and fio not in dictionary:
#             print('Такого сотрудника не существует!')
#             continue
#         dictionary[fio] = {}
#         for key in keys:
#             value = input(f'Введите {key} сотрудника: ')
#             dictionary[fio][key] = value
#         if command == '1':
#             print('Новый сотрудник успешно добавлен!')
#         else:
#             print('Данные о сотруднике успешно изменены!')
#     elif command == '2':
#         fio = input('Введите ФИО сотрудника через пробел: ')
#         del dictionary[fio]
#         print(f'Сотрудник {fio} удален!')
#     elif command == '3':
#         fio = input('Введите ФИО сотрудника через пробел: ')
#         if fio in dictionary:
#             print(f'Данные сотрудника: {fio}')
#             for key, value in dictionary[fio].items():
#                 print(f'{key} сотрудника: {value}')
#         else:
#             print('Такой сотрудник не зарегистрирован!')
#     else:
#         print('Такой команды нет! Завершаю работу...')
#         break

# -----------------------------------------------------------------

# Декораторы - функции, которые меняют поведение других функций,
# не внося изменений в код функций

# def pretty_output(func):
#     print('*'*5)
#     func()
#     print('*' * 5)
#     return 5
#
#
# @pretty_output
# def print_hi():
#     print('Hi!')
#
#
# print(print_hi)


# 1. Напишите декоратор logging, который будет вести
# логи вызова функции. В них он должен будет отображать
# аргументы и результат вызова функции.
# Пример:
# @logging
# def summa(a, b):
#     return a + b
#
# >>> summa(2, 3)
# Function summa was called with arguments: 2, 3 and returned 5

# Подсказка: Имя функции - это func.__name__
# print(print.__name__) -> 'print'

# def logging(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'Function {func.__name__} was called with arguments: '
#               f'{*args, kwargs} and returned {result}')
#         return result
#     return wrapper
#
#
# @logging
# def summa(a, b, c, d):
#     return a + b - c - d
#
#
# print(summa(2, 3, c=2, d=5))


# 2.

# Напишите декоратор, который измеряет время,
# необходимое для выполнения функции, и
# печатает время выполнения.


# def timer(func):
#     def wrapper(*args, **kwargs):
#         from time import time
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print(f'Function {func.__name__} runned in {round(end - start, 3)} seconds '
#               f'with these arguments: {*args, kwargs}')
#         return result
#     return wrapper
#
#
# @timer
# def create_random_list(num):
#     import random
#     return [random.randint(-num, num) for _ in range(num)]
#
#
# lst = create_random_list(1000000)
# print(lst[:5])


# def caching(func):
#     cache = {}
#
#     def wrapper(*args, **kwargs):
#         if (args, *kwargs.items()) not in cache:
#             cache[(args, *kwargs.items())] = func(*args, **kwargs)
#         return cache[(args, *kwargs.items())]
#     return wrapper
#
#
# @caching
# def cached_fibo(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return cached_fibo(n - 1) + cached_fibo(n - 2)
#
#
# def fibo(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
# print(cached_fibo(300))

# Декораторы с параметрами

# import random
#
#
# def retry(num=5):
#     def decorator(func):
#         count = 0
#
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             while count < num:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception:
#                     print('Функция не отработала!')
#                     count += 1
#             return 'Что-то пошло не так'
#         return wrapper
#     return decorator
#
#
# @retry()
# def random_function():
#     if random.randint(1, 2) == 1:
#         raise ValueError
#     return 'Функция отработала успешно!'
#
#
# print(random_function())


# 5.

# Напишите декоратор с именем validate_args,
# который принимает переменное количество
# аргументов, представляющих ожидаемые
# типы аргументов для декорированной функции.
# Декоратор должен вызывать TypeError,
# если какой-либо из аргументов имеет
# неправильный тип. Декоратор должен
# работать с функциями, имеющими любое
# количество аргументов.
#
# Например, если декорированная функция
# принимает два аргумента, целое число
# и строку, декоратор должен вызвать
# ошибку TypeError, если первый
# аргумент не является целым числом,
# а второй аргумент не является строкой.


# from typing import List


# def validate_args(*types):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             all_args = args + tuple(kwargs.values())
#             for type_of, arg in zip(types, all_args):
#                 if type_of != type(arg):
#                     raise TypeError(f'Expected {type_of.__name__}, got {type(arg).__name__} instead in {arg}')
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @validate_args(int, str)
# def print_some(a, string):
#     print('hello', a, string)
#
#
# print_some(4, 'new')


# Аннотации:
# def validate_args(func):
#     def wrapper(*args, **kwargs):
#         all_args = args + tuple(kwargs.values())
#         types = list(func.__annotations__.values())
#         print(types)
#         for type_of, arg in zip(types, all_args):
#             if type_of != type(arg):
#                 raise TypeError(f'Expected {type_of.__name__}, got {type(arg).__name__} instead in {arg}')
#         result = func(*args, **kwargs)
#         if type(result) == types[-1]:
#             return result
#         else:
#             raise TypeError(f'Expected function to return {types[-1].__name__}, got {type(result).__name__} instead.')
#
#     return wrapper
#
#
# @validate_args
# def print_some(a: list, string: str) -> int:
#     print('hello', a, string)
#     return 4
#
#
# print_some([4], 'new')
