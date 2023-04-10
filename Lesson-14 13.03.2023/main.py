# 1.
# string = 'Take me home'
# remove_vowels = lambda x: ''.join([char for char in x
#                                    if char not in 'eyuioa'])
# print(remove_vowels(string))

# 2.
# string = 'Takemehome'
# if_alpha = lambda x: x.isalpha()
# print(if_alpha(string))

# 3.
# lst = [1, 2, 6, 2, 3]
# product = lambda numbers: 1 if len(numbers) == 0 else \
#                           numbers[0] if len(numbers) == 1 else \
#                           numbers[-1] * product(numbers[:-1])
# print(product(lst))

# 4.
# lst = ['Окей', 'Пока', 'Ака', 'А роза упала на лапу Азора']
# get_palindromes = lambda strings: [string for string in strings
#                                    if string.replace(' ', '').lower()
#                                    == string[::-1].replace(' ', '').lower()]
# print(get_palindromes(lst))

# 5.
# is_prime = lambda x: len([x % i for i in range(2, int(x**0.5) + 1) if x % i == 0]) == 0
# print(is_prime(13))

# 6.
# factorial = lambda x: 1 if x == 1 else x * factorial(x - 1)
# print(factorial(5))


# -------------------------------------------------
# Словарь - dictionary(dict)
# print(dict)
# dict()/ {} / {'key': 'value'}

# test1 = {}
# print(type(test1)) - <class 'dict'>

# test = {'key': 'value'}
#
# print(test)

# Ключом словаря может быть только неизменяемый тип данных
# test = {[1]: 'value'} - Вернёт ошибку
# test = {(1,): 'value'} - Сработает

# test = {1: 2, 3: 4, 5: 6}
# print(test.keys())
# print(test.values())
# for i in test.values():
#     print(i)

# print(test.items())

# Автоматическая распаковка
# a, b = (1, 2)
# print(a, b)

# for key, value in test.items():
#     print(key, value)
# print(test)
# print(test.pop(5))
# test[7] = 8
# if 8 in test.values():
#     test[8] = 9

# print(test.get(5))
# print(test.popitem())
# print(test.setdefault(7, 7))
# print(test)
# test.update({7: 8, 9: 10})
# print(test)


# 1.

# numbers = {'x1': 5, 'x2': -2, 'x3': 4, 'x4': -1}
# product = 1
# for num in numbers.values():
#     product *= num
# print(product)


# 2.

# veggies = {}
# for i in range(1, 5):
#     veggies[i] = input('Введите название овоща: ')
#
# print(veggies)
# index = int(input('Введите, какой овощ удалить: '))
# del veggies[index]
# print(veggies)


# 3.

# person = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_dict = {'name': person.pop('name'), 'salary': person.pop('salary')}
# print(person)
# print(new_dict)


# 4.

# person = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# person['location'] = person.pop('city')
# print(person)

# 5.

# import random
#
# sells = {'John': {}, 'Tom': {}, 'Anne': {}, 'Fiona': {}}
# for key in sells.keys():
#     sells[key].update({'N': random.randint(1000, 9999),
#                        'S': random.randint(1000, 9999),
#                        'E': random.randint(1000, 9999),
#                        'W': random.randint(1000, 9999)})
#
# for key, value in sells.items():
#     print(key)
#     for direction, number in value.items():
#         print(f'{direction} : {number}')
#
# name = input('Имя: ')
# region = input('Регион: ')
# print(sells[name][region])
# new_value = int(input('Новое значение: '))
# sells[name][region] = new_value
# print(sells[name])

# 6.

# nums = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}

# 1
# while len(nums) > 2:
#     nums.popitem()
# print(nums)

# 2
# dict_list = dict(list(nums.items())[:2])
# print(dict_list)

