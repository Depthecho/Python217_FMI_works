# import time
# 1.
# def half(x):
#     return x // 2
#
# def is_even(x):
#     return x % 2 == 0
#
#
# def repeat_until(f, p):
#     def inner(x):
#         while not p(x):
#             x = f(x)
#         return x
#     return inner
#
#
# repeat_until_even = repeat_until(half, is_even)
# print(repeat_until_even(19))
# print(repeat_until_even(22))


# 2.

# def make_counter(num):
#     def inner():
#         nonlocal num
#         if num <= -1:
#             return 'Error: Counter has reached 0'
#         tmp = num
#         num -= 1
#         return tmp
#     return inner
#
#
# c = make_counter(3)
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())


# 3.

# def throttle(seconds, func):
#     last_call = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal last_call
#         if time.time() - last_call > seconds:
#             last_call = time.time()
#             return func(*args, **kwargs)
#         else:
#             print('You can\'t call that function that often')
#
#     return wrapper
#
#
# def print_hi(name):
#     print(f'Hi, {name}')
#
#
# throttled_print = throttle(2, print_hi)
# throttled_print('name')
# throttled_print('name2')
# time.sleep(2)
# throttled_print('name3')
# throttled_print('name4')
# throttled_print('name5')


# ---------------------------------------------------
# Алгоритмы сортировки
# from random import randint

# 1. Bubble sort - сортировка пузырьком

# Сложность алгоритма - O(n^2)


# def bubble_sort(array):
#     for i in range(len(array)):
#         for j in range(len(array) - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return array


# 2. Insert sort - Сортировка вставками

# Сложность алгоритма в худшем случае - O(n^2)
# Сложность алгоритма в среднем случае - O(n*log(n)))

# def insert_sort(array):
#     for i in range(1, len(array)):
#         key = array[i]
#         j = i
#         while key < array[j - 1] and j > 0:
#             array[j] = array[j - 1]
#             j -= 1
#         array[j] = key
#
#     return array


# 3. Merge sort - Сортировка слиянием

# Сложность алгоритма в худшем случае - O(n^2)
# Сложность алгоритма в среднем случае - O(n*log(n)))

# def merge_sort(array):
#     if len(array) <= 1:
#         return array
#     left = merge_sort(array[:len(array) // 2])
#     right = merge_sort(array[len(array) // 2:])
#     n = m = k = 0
#     result = [0] * len(array)
#
#     while n < len(left) and m < len(right):
#         if left[n] < right[m]:
#             result[k] = left[n]
#             n += 1
#         else:
#             result[k] = right[m]
#             m += 1
#         k += 1
#
#     while n < len(left):
#         result[k] = left[n]
#         n += 1
#         k += 1
#
#     while m < len(right):
#         result[k] = right[m]
#         m += 1
#         k += 1
#
#     return result


# 4.

# Shell sort - Сортировка Шелла
# Худшее время - O(n^2)
# Лучшее время O(n * log^2n)
# При оптимальном наборе шагов(Седжвика) O(n^(4/3))

# import math
#
#
# def shell_sort(array):
#     k = int(math.log2(len(array)))
#     interval = 2**k - 1
#     while interval > 0:
#         for i in range(interval, len(array)):
#             key = array[i]
#             j = i
#             while j >= interval and array[j-interval] > key:
#                 array[j] = array[j - interval]
#                 j -= interval
#             array[j] = key
#         k -= 1
#         interval = 2**k - 1
#
#     return array


# test = False
#
# if test:
#     from time import time
#     size = 10000
#     nums = [randint(-size, size) for i in range(size)]
#     functions = [bubble_sort, insert_sort, merge_sort, shell_sort, list.sort, sorted]
#
#     print('На наборе случайных значений: ')
#     for func in functions:
#         start = time()
#         func(nums.copy())
#         end = time()
#         print(f'Функция {func.__name__} отработала за {end - start} секунд')
#
#     nums = [i for i in range(size)]
#     print('На наборе отсортированных значений: ')
#     for func in functions:
#         start = time()
#         func(nums.copy())
#         end = time()
#         print(f'Функция {func.__name__} отработала за {end - start} секунд')
#
#     nums.reverse()
#     print('На обратном наборе отсортированных значений: ')
#     for func in functions:
#         start = time()
#         func(nums.copy())
#         end = time()
#         print(f'Функция {func.__name__} отработала за {end - start} секунд')


# Задача 3
# n = 10
# numbers = [randint(1, n) for i in range(n)]
# print(numbers)
#
# half = len(numbers) // 2
# for i in range(1, len(numbers)):
#     key = numbers[i]
#     j = i
#     if j < half:
#         while key > numbers[j - 1] and j > 0:
#             numbers[j] = numbers[j - 1]
#             j -= 1
#     else:
#         while key < numbers[j - 1] and j > half:
#             numbers[j] = numbers[j - 1]
#             j -= 1
#     numbers[j] = key
#
# print(numbers)
