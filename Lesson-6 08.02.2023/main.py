# Списки - это упорядоченный тип данных
#           0       1        2
# names = ['Egor', 'Vadim', 'Vanya']
# print(names)
# print(names[0])  # Правила работы индексов у списков аналогичны строкам
# print(names[:2])  # Правила работы срезов у списков аналогичны строкам

# Списки - это изменяемый тип данных
# names = ['Egor', 'Vadim', 'Vanya']
# names[0] = 0  # Замена по индексу возможна, в отличие от строк
# print(names)

# Списки - это не уникальный тип данных
# nums = [0, 0, 0]
# print(nums)

# nums = list((0, 0, 0))
# print(nums)

# Вследствие того, что в Python неявная и динамическая типизация
# в списке могут храниться данные разных типов:
# spisok = [1, 'Egor', True, [1, 2, 3]]
# print(spisok)

### Методы добавления элементов в список
# nums = [1, 2, 3]
# print(nums)
# nums.append((4, 5))
# print(nums)
# nums.insert(6, 5)
# print(nums)
# nums.extend((4, 5, 6))
# print(nums)


### Методы удаления элементов из списка

# spisok = [1, 2, 3, 4]
# a = spisok.pop(-3)
# print(spisok, a)
#
# spisok.remove(2)
# print(spisok)

# 1.
# nums = [1, 2, 3, 4, 5, 6, 7]
#
# print(nums[:])
# print(nums[::-1])
# print(nums[::2])
# print(nums[1::2])
# print(nums[:1])
# print(nums[6:])
# print(nums[3:4])
# print(nums[4:])
# print(nums[4:1:-1])
# print(nums[-3:-6:-1])
# print(nums[2:5])


# 2.
# squares = []
# for i in range(1, 11):
#     squares.extend([i**2])
# print(squares)


# nums = [1, 2, 3, 4, 5, 6]

# Мы используем, когда хотим получить доступ к ячейкам списка
# for i in range(len(nums)):
#     print(nums[i], end=' ')

# Мы используем, когда хотим получить доступ к значениям списка
# for num in nums:
#     print(num, end=' ')

# Пример с умножением
# nums = [1, 2, 3]
# for i in range(len(nums)):
#     nums[i] *= 2
# print(nums)
#
# nums = [1, 2, 3]
# for num in nums:
#     num *= 2
# print(nums)


# Случайность в Python
# import random
#
# print(random.randint(1, 100))
# print(random.random())

# Выражение for Переменная in range()|_Iterable (Далее необязательное условие) if Выражение
# x for x in range(n)

# nums = [i for i in range(5) if i % 2 == 0]
# print(nums)

# print(i for i in range(5))

# 3.

# nums = []
# length = int(input('Введите количество чисел: '))
# for i in range(length):
#     num = int(input('Введите число кратное 3: '))
#     if num % 3 == 0:
#         nums.append(num)
#     else:
#         print(f'{num} не делится на 3 без остатка!')
# print(nums)


# Стандартные функции, полезные для списков
# nums = [1, 2, 3, 5, 'name']
# print(sum(nums))
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sorted(nums, reverse=True))


# 4.
# nums = [int(input('-> ')) for i in range(int(input('n = ')))]
# nums.pop(int(input('Введите индекс: ')))
# print(nums)


# 5.
# nums = [int(input('-> ')) for i in range(int(input('n = ')))]
# nums.remove(int(input('Введите элемент: ')))
# print(sorted(nums, reverse=True))


# 6.
# import random
# random_numbers = [random.randint(1, 100) for i in range(10)]
# print(random_numbers)
# maximum = max(random_numbers)
# print(f'Max: {maximum}')
# random_numbers.remove(maximum)
# random_numbers.insert(0, maximum)
# print(random_numbers)
