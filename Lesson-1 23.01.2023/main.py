# name = input('Введите ваше имя: ')
# print('Hello', name)

# print('123')  # Тут выводится 123
# При именовании переменных используем a-z, A-Z, '_', 1-0
# camelCase | snake_case

# print('123')
# print = 5

# True = 5 - Так делать нельзя
# import keyword
# print(keyword.kwlist)

# print('Hello')
# print("Hello")
# print('''Hello''')

# +, -, *, /
# // - целочисленное деление
# % - остаток от деления
# ** - степень

# В Python абсолютно всё - это объекты

# int(integer - целое число) - целые числа: 6, 1, 14, -6
# str(string - нить/строка) - строки: '124', '54safas'
# float(floating point - плавающая точка/запятая) - дробные числа: 6.24, 9.0, -15.2411
# bool(boolean - булевый) - логические значения - True, False

# name = 123
# print(type(name))
# name = 'Egor'
# print(type(name))

# Неявная сильная динамическая типизация
# a = 5
# b = 7.5
# name = 'Egor'
# c = True
# print(name + a)
# print(name - a)
# print(a + b)
# print(a + c)
# print(a * name)
# print(a / 1)

# print(name + str(a))
# print(int('5.6'))
# print(int(5.9))
# print(float('6.125'))
# print(float(5))
# print(bool(''))  # Пустая строка
# print(bool(0))
# print(bool(False))
# print(bool(None))  # Обозначение отсутствия чего-либо
# Все остальные значения преобразуются в True

# name = 'Egor'
# age = 20
# print('Hello ' + name + " and I'm " + str(age))
# print('Hello', name, "and I'm", age)
# print(f"Hello {name} and I'm {age}")

# string = 'Hello\nWorld!'
# print(string)

# print('Hello, I\'m Djo')

# win + V - буфер обмена

# REPL - Read -> Evaluate -> Print -> Loop

# print('Hello')
# pr = print
# pr('Hello')

# age = 20
# print(id(age))
# his_age = 20
# print(id(his_age))
# age = 10
# print(id(age))
# print(id(his_age))
# del age

# print(id(print))
# name = print
# print(id(name))