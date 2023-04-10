# num = int(input('Введите четырехзначное число: '))
# num1 = num // 1000
# num2 = (num // 100) % 10
# num3 = (num // 10) % 10
# num4 = num % 10
# print(num1 * num2 * num3 * num4)

# num = int(input('Введите четырехзначное число: '))
# print(str(num)[::-1])
# num1 = num // 1000
# num2 = (num // 100) % 10
# num3 = (num // 10) % 10
# num4 = num % 10
# print(num4 * 1000 + num3 * 100 + num2 * 10 + num1)


# print('123' - исключения, срабатывающие до начала программы (SyntaxError)

# print(1 + '1') - исключения, срабатывающие во время работы программы (TypeError)

# каноничный пример использования try - except
# try:
#     age = int(input('Введите свой возраст: '))
# except ValueError:
#     print('Вы ввели что-то не так')


# try:
#     apples = int(input('Сколько у вас яблок? '))
#     people = int(input('Сколько вас человек? '))
#     print(f'Каждый человек получит по {apples/people} яблок')
# except ValueError:
#     print('Вы неверно ввели число, используйте цифры')
# except Exception:
#     print('Какое-то исключение')
# except ZeroDivisionError:
#     print('Вас не может быть 0 человек!!')

# try:
#     apples = int(input('Сколько у вас яблок? '))
#     people = int(input('Сколько вас человек? '))
#     if apples < 0 or people < 0:
#         raise ValueError
#     print(f'Каждый человек получит по {apples/people} яблок')
# except ValueError:
#     print('Ошибка ввода данных! Данные должны быть '
#           'больше 0 и в цифровом виде')

# try:
#     apples = int(input('Сколько у вас яблок? '))
#     people = int(input('Сколько вас человек? '))
#     print(f'Каждый человек получит по {apples/people} яблок')
# except ValueError:
#     print('Вы неверно ввели число, используйте цифры')
# except ZeroDivisionError:
#     print('Вы неверно ввели число, используйте цифры')
# finally:
#     print('Я в любом случае тут')


# 1. Напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться
# конкатенация, то есть соединение строк. В остальных случаях
# введённые числа суммируются.
#
# try:
#     a = input('Введите число: ')
#     b = input('Введите число: ')
#     a = int(a)
#     b = int(b)
#     print(a + b)
# except ValueError:
#     a = str(a)
#     print(a + b)

# a = 0
# while a < 100:
#     print(a)
#     a += 1  # аналогично a = a + 1. Существуют также -=, *=, /= и т.д.


# a = 0
# while True:
#     print('Я работаю бесконечно', a)
#     a += 1

# 2. Пользователь вводит два числа. Выведите все числа в диапазоне
#
# start, end = int(input('Введите начало: ')), int(input('Введите конец: '))
# while start <= end:
#     print(start)
#     start += 1

# 3. Пользователь вводит два числа. Выведите все четные числа в диапазоне
#
# start, end = int(input('Введите начало: ')), int(input('Введите конец: '))
# if start % 2 == 1:
#     start += 1
# while start <= end:
#     print(start)
#     start += 2

# 3. Пользователь вводит два числа. Если числа введены в обратном порядке,
# поменяйте их. Выведите все четные числа в диапазоне
#
# start, end = int(input('Введите число: ')), int(input('Введите число: '))
# if start > end:
#     start, end = end, start
# while start <= end:
#     if start % 2 == 0:
#         print(start)
#     start += 1


# while True:
#     answer = input('Какое ваше следующее действие?...'
#                    '(Введите "0", чтобы выйти) ')
#     if answer == '0':
#         break

# a = 0
# while a < 10:
#     a += 1
#     if a > 5:
#         continue
#     print(f'{a} Я!')

# a = 1
# while a <= 10:
#     print(a)
#     a += 1
#     answer = input('Хотите ли вы закончить? ')
#     if answer == 'да':
#         break
# else:
#     print('Цикл завершился нормальной работой')


# 4. Пользователь вводит с клавиатуры длину линии.
# Нужно отобразить на экране горизонтальную линию
# из *, указанной длины. Например, если было введено 7,
# тогда вывод на экран будет такой: *******
#
# Решение 1
# a = int(input('Введите число: '))
# i = 0
# while i < a:
#     print('*', end='')
#     i += 1
# Решение 2
# result = ''
# i = 0
# while i < a:
#     result += '*'
#     i += 1
# print(result)

# 5. Пользователь вводит с клавиатуры два числа. Нужно
# посчитать сумму нечетных чисел в указанном диапазоне.
#
# a, b = int(input('Введите начало: ')), int(input('Введите конец: '))
# summa = 0
# while a <= b:
#     if a % 2 == 1:
#         summa += a
#     a += 1
# print(summa)

# 6. Написать программу – конвертер валют. Реализовать
# общение с пользователем через меню.
#
# while True:
#     source_currency = input('Введите, какую валюту вы хотите перевести')
#     target_currency = input('Введите, В какую валюту вы хотите перевести')
#     amount = int(input('Введите размер перевода: '))
#     if source_currency == 'доллар':
#         if target_currency == 'рубль':
#             print(f'{amount} долларов в рубли: {amount * 70}')
#         elif target_currency == 'евро':
#             print(f'{amount} долларов в евро: {amount / 0.95}')
#         elif target_currency == 'юань':
#             print(f'{amount} долларов в юани: {amount * 7}')
#     elif source_currency == 'рубль':
#         if target_currency == 'доллар':
#             print(f'{amount} рублей в доллары: {amount / 70}')
#         elif target_currency == 'евро':
#             print(f'{amount} рублей в евро: {amount / 75}')
#         elif target_currency == 'юань':
#             print(f'{amount} рублей в юани: {amount / 10}')
#     elif source_currency == 'евро':
#         if target_currency == 'доллар':
#             print(f'{amount} евро в доллары: {amount * 1.05}')
#         elif target_currency == 'рубль':
#             print(f'{amount} евро в рубли: {amount * 75}')
#         elif target_currency == 'юань':
#             print(f'{amount} евро в юани: {amount * 7.5}')
#     elif source_currency == 'юань':
#         if target_currency == 'доллар':
#             print(f'{amount} юаней в доллары: {amount / 7}')
#         elif target_currency == 'рубль':
#             print(f'{amount} юаней в рубли: {amount * 10}')
#         elif target_currency == 'евро':
#             print(f'{amount} юаней в евро: {amount / 7.5}')
#     quiting = input('Хотите ли вы выйти?')
#     if quiting == 'да':
#         break