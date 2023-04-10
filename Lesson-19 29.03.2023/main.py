# 1.
# import random
#
# nums = [random.randint(-10, 10) for i in range(10)]
#
# print(nums)
# mean = sum(nums) / len(nums)
# sorting_flag = len(nums) // 3
# if mean > 0:
#     sorting_flag *= 2
# start = nums[:sorting_flag]
# start.sort()
# nums = start + nums[sorting_flag:][::-1]
# print(nums)
import re

# 3.

# import random
# nums = [random.randint(-10, 10) for i in range(10)]
# print(nums)
# count = 0
# for i in range(len(nums)):
#     swapped = False
#     for j in range(len(nums) - 1):
#         count += 1
#         if nums[j] > nums[j + 1]:
#             swapped = True
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     if not swapped:
#         break
#
# print(nums, count)


## Регулярные выражения - regular expression/regexp/regex
# import re
#
# string = '12345@mail.ru'
# result = re.search('\d?', string)
# print(result.group())
# print(result.start())  # | end()
# print(result.span())
# print(result)


# import re
# phone_number = '+79564275242'
# result = re.search('[+]?\d+', phone_number)

# string = '123456'
# result = re.match('2\d+', string)

# string = '1zxg2z3as45xvz6'
# result = re.findall('\d+', string)

# string = '1zxg2z3as45xvz6'
# result = re.finditer('\d+', string)
#
# for i in result:
#     print(i)

# string = "Я. Ты! Она? Он..."
# result = re.split('[.!?\s]+', string)
# print(result)


# 1.
# import re
# name = 'Час в 24-часовом формате от 00 до 23. ' \
#        '2021-06-15Т23:59. Минуты, в диапазоне от ' \
#        '00 до 59. 2021-06-15Т01:09.'

# result = re.findall(r'\d{2}:\d{2}', name)
# print(result)

# С учетом человеческого времени
# result = re.finditer(r'([01]\d|2[0-3]):[0-5]\d', name)
# print([i.group() for i in result])


# 2.
# import re
#
# numbers = '+7 912 532-53-11, 79125325311, 7 (912) 532 53 11, +79125322311'
# result = re.findall('\+?7\d{10}', numbers)
# print(result)


# 3.

# import re
# emails = ['123456@i.ru', '123_456@ru.name.ru', 'login@i.ru',
#           'norwH-1@i.ru', 'login.3@i.ru', 'Login.3-67@i.ru',
#           '1login@ru.name.ru']
# for email in emails:
#     result = re.fullmatch('[\w.-]+@[\w.]+\.ru', email)
#     print(result)


# 4.

# import re
# string = "(в русском языке встречаются названия питон[16] " \
#          "или пайтон[17]) — высокоуровневый язык программирования " \
#          "общего назначения с динамической строгой типизацией и " \
#          "автоматическим управлением памятью[18] [19]."
# res = re.findall('\[\d+]', string)
# print(res)


# 5.

# while True:
#     date = input('Введите дату в формате dd-mm-YYYY: ')
#     result = re.fullmatch('(0[1-9]|[12]\d|3[01])[-/:.](0[1-9]|1[0-2])[-/:.]\d{4}', date)
#     print(result)


# import re
# re.search / re.match / re.fullmatch / re.findall / re.finditer
# re.split
# Квантификаторы количества {n, m}(n и m опциональны), ?(0 или 1), *(0 или более), +(1 или более)
# Шаблоны \d(любая цифра), \w(любая буква или любая цифра или _),
# \s(любой пробельный символ: пробел, таб, перенос строки)

# 1.
# Напишите регулярное выражение, которое соответствует
# всем строкам, начинающимся с гласной и заканчивающимся
# на согласную.

# 2.
# Напишите регулярное выражение, которое соответствует
# всем URL-адресам.

# 3.
# Напишите регулярное выражение, которое соответствует
# всем строкам, содержащим хотя бы одно слово,
# начинающееся с заглавной буквы.

# 4.
# Напишите регулярное выражение, которое соответствует
# всем строкам, содержащим повторяющуюся букву (например,
# «book» или «letter»).
