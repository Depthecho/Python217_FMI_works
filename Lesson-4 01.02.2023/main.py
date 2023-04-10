# i = 1
# while i < 6:
#     print(i)
#     i += 1

# for name in ['Егор', 'Кирилл', 'Маша', 'Алина']:
#     print(name)

# for _ in range(5):
#     print('Hello there')

# for i in range(2, 5):
#     print(i)

# for i in range(2, 11, 2):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# greet = "Hello there"
# for i in greet:
#     print(i)


# num = int(input('Введите число: '))
# for i in range(1, 10):
#     print(f'{num} * {i} = {num * i}')

# num = int(input('Введите число: '))
# for j in range(num):
#     for i in range(num):
#         print('*', end='\t')
#     print()

# Вывести на экран таблицу умножения
# for j in range(1, 10):
#     for i in range(1, 10):
#         print(f'{i} * {j} = {i * j}', end='\t')
#     print()


# for i in range(1, 10):
#     print(i)
# else:
#     print('Я полностью отработал')


# for i in range(3):
#     for j in range(6):
#         print('*', end='')
#     print()

# !ТЕРНАРНЫЙ ОПЕРАТОР!
# age = int(input('Сколько вам лет?'))
# can_drive = 'да' if age > 17 else 'нет'
# !ТЕРНАРНЫЙ ОПЕРАТОР!

# Необходимо вывести на экран прямоугольник
# из чередующихся символов.
# for i in range(4):
#     for j in range(10):
#         if (i + j) % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#     print()


# print('HelloHelloHello')
# print('Hello' * 3)

# Вывести диагональ из звёздочек
# for i in range(6):
#     print(i * ' ' + '*')

# Пользователь вводит целое число. Необходимо
# вывести все целые числа, на которые заданное
# число делится без остатка
# num = int(input('Введите число:'))
# for i in range(1, num//2 + 1):
#     print(f'{i} ' if num % i == 0 else '', end='')



# Пользователь вводит число. Определить количество
# цифр в этом числе, посчитать их сумму и среднее арифметическое.
# Определить количество нулей в этом числе.
# Общение с пользователем организовать через меню.
# while True:
#     num = int(input('Введите число(0 для выхода): '))
#     if num == 0:
#         break
#     zeros = 0
#     summa = 0
#     digits = 0
#     while num != 0:
#         last = num % 10
#         summa += last
#         digits += 1
#         if last == 0:
#             zeros += 1
#         num //= 10
#     print(f'Количество цифр: {digits}\n'
#           f'Количество нулей: {zeros}\n'
#           f'Среднее значение цифр: {summa/digits}\n'
#           f'Сумма цифр: {summa}\n')

# num = 4
# for i in range(1, num):
#     print(' ' * (num - i) + '*' * i * 2)
# for i in range(num, 0, -1):
#     print(' ' * (num - i) + '*' * i * 2)


# width, height = int(input('Введите ширину: ')), \
#                 int(input('Введите высоту: '))
# for i in range(height):
#     if i == 0 or i == height - 1:
#         print(width * '*')
#     else:
#         print('*' + (width - 2) * ' ' + '*')
