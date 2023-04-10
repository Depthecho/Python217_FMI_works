# ASCII
# 2^7 - 128

# UTF-8 - 8 бит для кодировки символа
# name = 'Henry Быстрый'
# print(name.encode(encoding='utf-8'))
# 16-чная система счисления использует 0-9 и a,b,c,d,e,f

# name = 'hello'  # (h - 0, e - 1, l - 2, l - 3, o - 4)
# print(name[4])  #     -5,    -4,    -3,    -2,    -1
# print(name[-5])

# name = 'hello'
# name[0] = 'c' - невозможно изменить строку

# name = 'George'
# print(name[0] + name[1] + name[2])
# print(name[0:3])

# for i in range(1, 5, 2)

# name = 'George'
# print(name[::-1]) - популярный вариант разворота строки
# print(name[5:1])


### Методы управления регистром строк
# my_str = "python was created in the late 1980's " \
#          "by Guido van Rossum."

# print(my_str.upper())  # - делает все символы в строке заглавными
# print(my_str.lower())  # - делает все символы в строке строчными

# print(my_str.capitalize())  # - делает первую букву в строке заглавной, а остальные строчными
# print(my_str.title())  # - делает заглавной первую букву каждого слова в строке
# print(my_str.swapcase())  # - меняет регистр букв на обратный


### Методы поиска по строкам

# my_str = "Python was created in the late 1980's " \
#          "by Guido van Rossum. Python - cool!"

# Находит первое вхождение подстроки в данной строке
# Поддерживает указание границ поиска(начало и конец)
# print(my_str.find('   '))
# print(my_str.find('python', 10, 20))

# Работает аналогично методу find, но выбрасывает
# исключение при отсутствии результатов поиска
# print(my_str.index('python'))
# print(my_str.index('python', 10, 20))

# Методы, аналогичные вернхим, но которые ищут с конца строки
# print(my_str.rfind('Python'))
# print(my_str.rindex('Python'))

# Метод, позволяющий посчитать количество вхождений подстроки в строке
# print(my_str.count('Python'))


### Методы проверки содержимого строки

# my_str = "Python was created in the late 1980's " \
#          "by Guido van Rossum. Python - cool!"

# Проверяет, что строка начинается с указанной подстроки
# print(my_str.startswith('P'))

# Проверяет, что строка кончается на указанную подстроку
# print(my_str.endswith('!'))

# str1 = '123'
# str2 = 'Имя'
# str3 = 'name123'
# str4 = '5.5'

# print(str3.isdigit())  # - is digital
# print(str3.isalpha())  # - is alphabetical
# print(str3.isalnum())  # - is alphabetical or numerical
# print(str4.isdigit())

# str3 = 'name123'
# for char in str3:
#     print(char.isdigit())

# str3 = 'name123'

# print(str3.islower())  # проверяет, что символы в строке маленькие
# print(str3.isupper())  # проверяет, что символы в строке большие


### Методы форматирования строк

# name = 'Philipp'

# Центрирует строку по указанной ширине и заполняет пустоту указанным символом
# print(name.center(20, '@'))

# Выравнивают строку по левому и правому краю, соответственно
# Аналогично методу center
# print(name.ljust(20, '$'))
# print(name.rjust(20, '$'))

# greet = '\tHello, traveler'
# print(greet)  # Заменяет табы на пробелы в указанном количестве
# print(greet.expandtabs(4))

# name = '    Egor   '
# Методы, удаляющие пробелы(если не указан другой символ) с краев строки

# print(name.strip('#'))
# print(name.lstrip())
# print(name.rstrip())


# Заменяет все вхождения строки 'Hello' на строку 'Oh'
# Если указано количество, останавливается после этих замен
# name = 'Hello'
# name = name.replace('Hello', 'Oh', 1)
# print(name)

# name = 'Hello, I\'m Kevin'
# print(name)

# name = 'This facility named \\Python\\'
# print(name)

# name = r'\'  # сырая строка, которая невозможна
# print(name)

# 1.
# print(input('Введите строку: ')[::-1])


# 2.
# text = input('Введите строку: ')
# nums = 0
# letters = 0
# for symbol in text:
#     if symbol.isdigit():
#         nums += 1
#     elif symbol.isalpha():
#         letters += 1
# print('Буквы: ', letters)
# print('Цифры: ', nums)

# 3.
# string = input('Введите строку: ')
# target = input('Введите искомый символ: ')
# print(f'В строке {string}, символ {target} встречается'
#       f' {string.count(target)} раз')

# 4.

# string = input('Введите строку: ')
# target = input('Введите искомое слово: ')
# replacement = input('Введите слово на замену: ')
#
# print('Ваш текст после замены: ')
# print(string.replace(target, replacement))


# name = 'Egor'

# if 'e' in name:
#     print('It\'s there!')

# import string
#
# print(string.digits)
# print(string.ascii_letters)
# print(string.punctuation)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.ascii_lowercase)


# 5.
#
# text = input('Введите текст: ')
# print('Инструкция:'
#       '\nСделать(1) каждое предложение с заглавной буквы'
#       '\nПосчитать(2), сколько раз цифры встречаются в тексте'
#       '\nПосчитать(3), сколько раз знаки препинания встречаются в тексте'
#       '\nПосчитать(4) количество восклицательных знаков'
#       '\nВыйти(5)')
#
# while True:
#     command = input('Введите, что сделать с текстом: ')
#     if command == '5':
#         break
#     elif command == '1':
#         words = text.split()
#         words[0].capitalize()
#         for i in range(len(words)):
#             if words[i][-1] in '.!?' and i < len(words) - 1:
#                 words[i + 1] = words[i + 1].title()
#         text = ' '.join(words)
#         print(f'Новый текст: \n {text}')
#     elif command == '2':
#         count = 0
#         for i in text:
#             if i.isdigit():
#                 count += 1
#         print(f'Количество цифр в тексте: {count}')
#     elif command == '3':
#         count = 0
#         for i in text:
#             if i in ',.!?:;':
#                 count += 1
#         print(f'Количество знаков препинания в тексте: {count}')
#     elif command == '4':
#         print(f'Количество восклицательных знаков в тексте: {text.count("!")}')

