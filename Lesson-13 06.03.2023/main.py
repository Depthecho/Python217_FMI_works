# ---------------Домашнее задание----------------
# 1.

# def nod(a, b):
#     if b == 0:
#         return a
#     else:
#         return nod(b, a % b)
#
#
# print(nod(24, 15))


# 2.
# from random import randint
#
# def bulls_and_cows(number=str(randint(1000, 9999)), turn=1):
#     print(number)
#     guess = input(f'Ход {turn}. Введите число(1000-9999): ')
#     cows, bulls = 0, 0
#     temp_number = number
#     for i in range(3, -1, -1):
#         if guess[i] == number[i]:
#             cows += 1
#             temp_number = temp_number[:i] + temp_number[i + 1:]
#             guess = guess[:i] + guess[i + 1:]
#     for i in range(len(guess)-1, -1, -1):
#         if guess[i] in temp_number:
#             bulls += 1
#             digit = temp_number.find(guess[i])
#             temp_number = temp_number[:digit] + temp_number[digit + 1:]
#             guess = guess[:i] + guess[i + 1:]
#     if cows == 4:
#         print(f'Ты победил! Я загадал число: {number}')
#         print(f'Это заняло {turn} ходов.')
#         return
#     else:
#         print(f'Коровы: {cows} | Быки: {bulls}')
#         bulls_and_cows(number, turn + 1)
#
# bulls_and_cows()

# ---------------------------------------------------------
# tuple()
# a = tuple((1, 2, 3))

# a = (1, 2)
# print(a)

# a = 1, 2, 3
# a[0] = 0
# print(a)
# print(a[1])
# print(a.count(2))
# print(a.index(2))

# a = 1, 2, 3
# print(a[2])
# a = 3, 2, 1
# print(a)


# 1.

# fruits = ('apple', 'banana', 'apple', 'pear')
# fruit = input('Input name of fruit: ')
# print(f'There are {fruits.count(fruit)} {fruit} in fruits')


# 2.

# fruits = ('apple-pear', 'banana-strawberry', 'apple', 'pear', 'apple-grape')
# fruit = input('Input name of fruit: ')
# count = sum([fruit in cocktail for cocktail in fruits])
# print(f'There are {count} {fruit} in fruits')


# 3.

# auto = ('volvo', 'nissan', 'reno', 'jeep', 'volvo')
# mark, replacement = input('Введите, какую марку заменить: '), input('Введите, на что заменить: ')
# auto = tuple(car if car != mark else replacement for car in auto)
# print(auto)


# ---------------------------------------------
# set()
# a = {1, '2', 1}
# a = set('hello')
# b = set('world')
#
# print(a.union(b))  # объединение
# print(a.difference(b))  # вычитание
# print(a.intersection(b))  # пересечение

# a = set('hello')
# print(a.pop())

# import random
# b = set(random.randint(1, 10) for i in range(10))
# print(b)

# c = set(i*i for i in range(20))
# print(c)

# a = {1, 2}
# a.update({4})
# print(a.isdisjoint({2, 4}))
# a.discard(4)
# a.add(5)
# a.remove(2)
# print(a)


# 1.

# first_set = {'Москва', 'Питер', 'Новгород', 'Вологда'}
# second_set = {'Москва', 'Архангельск', 'Калининград', 'Новгород'}
# print(first_set.intersection(second_set))

# 2.

# first_set = {'Москва', 'Питер', 'Новгород', 'Вологда'}
# second_set = {'Москва', 'Архангельск', 'Калининград', 'Новгород'}
# print(first_set.difference(second_set))

# 3.

# countries = {'Англия', 'Франция', 'Япония', 'Германия', 'Финляндия'}
# print('Команды:\n'
#       '1. Добавить страну\n'
#       '2. Удалить страну\n'
#       '3. Найти страну\n'
#       '4. Проверить, есть ли страна')
#
# while True:
#     command = input('Введите номер команды: ')
#     if command == '1':
#         country = input('Введите страну: ')
#         countries.add(country)
#         print('Страна успешно добавлена!')
#     elif command == '2':
#         country = input('Введите страну: ')
#         if country in countries:
#             countries.remove(country)
#             print('Страна успешно удалена!')
#         else:
#             print('Такой страны нет!')
#     elif command == '3':
#         start = input('Введите символ/ы: ')
#         print(*[country for country in countries if country.startswith(start)])
#     elif command == '4':
#         country = input('Введите страну: ')
#         if country in countries:
#             print('Такая страна существует!')
#         else:
#             print('Такой страны нет!')
#     elif command == '0':
#         print('Пока!')
#         break
#     else:
#         print('Такой команды не существует!')


# 4.
# Создайте множество кортежей, где каждый кортеж
# содержит имя учащегося и его оценку
# за тест. Напишите программу, которая
# находит трех лучших учеников
# на основе их результатов.

# import random
#
# students = {(input('Введите имя: '), random.randint(60, 100)) for i in range(5)}
# print(students)
# top_students = sorted(students, key=lambda x: x[1])[-3:]
#
# print(top_students)
