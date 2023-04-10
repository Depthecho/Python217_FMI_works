# 1.
# def positive_return(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return 0 if result < 0 else result
#     return wrapper
#
#
# @positive_return
# def summa(a, b):
#     return a + b
#
#
# print(summa(2, -3))
# print(summa(2, 3))
# print(summa(-2, -3))


# 2.
# def run_other(other_func):
#     def decorator(target_func):
#         def wrapper(*args, **kwargs):
#             return other_func(target_func(*args, **kwargs))
#         return wrapper
#     return decorator
#
#
# def square(x):
#     return x**2
#
#
# @run_other(square)
# def summa(a, b):
#     return a + b
#
#
# print(summa(2, 3))
# print(summa(2, 2))


# 3.

# ???

# ------------------------------------------------------
# Линейный поиск O(n)
# Бинарный поиск O(log(n))

# Пример линейного поиска
# nums = [i for i in range(10000)]
# for num in nums:
#     if num == 8963:
#         print('Найдено!')


# Пример бинарного поиска
# import random
# start = 1
# end = 10000
# nums = [i for i in range(start, end + 1)]
# rand = random.randint(start, end)
#
# count = 0
# while start < end:
#     count += 1
#     current = (start + end) // 2
#     if current > rand:
#         end = current - 1
#     elif current < rand:
#         start = current + 1
#     else:
#         print(current, count)
#         break


## Сортировки
# Быстрая сортировка

# def quick_sort(array):
#     left = []
#     equal = []
#     right = []
#
#     if len(array) > 1:
#         pivot = array.pop(0)
#         for i in array:
#             if i < pivot:
#                 left.append(i)
#             elif i > pivot:
#                 right.append(i)
#             else:
#                 equal.append(i)
#         return quick_sort(left) + equal + quick_sort(right)
#     else:
#         return array
#
#
# import time
# import random
# start = time.time()
# quick_sort([random.randint(-10000, 10000) for i in range(10000)])
# print(time.time() - start)


# Пирамидальная сортировка
# Сложность O(n*log(n))

# def heap_sort(array):
#     def build_max_heap(lst):
#         length = len(lst)
#         start = (length - 2) // 2
#         while start >= 0:
#             max_heapify(lst, index=start, size=length)
#             start -= 1
#
#     def max_heapify(lst, index, size):
#         left = index * 2 + 1
#         right = index * 2 + 2
#         if left < size and lst[left] > lst[index]:
#             largest = left
#         else:
#             largest = index
#         if right < size and lst[right] > lst[largest]:
#             largest = right
#         if largest != index:
#             lst[largest], lst[index] = lst[index], lst[largest]
#             max_heapify(lst, largest, size)
#
#     build_max_heap(array)
#     for i in range(len(array) - 1, 0, -1):
#         array[0], array[i] = array[i], array[0]
#         max_heapify(array, index=0, size=i)
#
#
# import time
# import random
# start = time.time()
# nums = [random.randint(-10000, 10000) for i in range(10000)]
# heap_sort(nums)
# print(time.time() - start)


# ------------------------------------------------------------
# 1.

# def pancake_sort(pancakes):
#     sorted_index = 0
#     while pancakes != sorted(pancakes, reverse=True):
#         unsorted_part = pancakes[sorted_index:]
#         max_index = unsorted_part.index(max(unsorted_part))
#
#         top = unsorted_part[max_index:][::-1]
#         unsorted_part = (unsorted_part[:max_index] + top)[::-1]
#
#         pancakes = pancakes[:sorted_index] + unsorted_part
#         sorted_index += 1
#     return pancakes


# import time
# import random
# start = time.time()
# nums = [random.randint(1, 10000) for i in range(10000)]
# pancake_sort(nums)
# print(time.time() - start)


from random import randint

lists = [[randint(-20, 20) for i in range(10)] for j in range(4)]
for lst in lists:
    print(*lst)
final_list = []
for lst in lists:
    for num in lst:
        if lst.count(num) == 1:
            final_list.append(num)
sorting = input('Отсортировать список по убыванию(1) или по возрастанию(2)? ')
final_list.sort(reverse=sorting == '1')
num = int(input('Введите значение для поиска: '))
left = 0
right = len(final_list) - 1
while left < right:
    current = (left + right) // 2

    if (final_list[current] > num and sorting == '1') \
            or (final_list[current] < num and sorting == '2'):
        left = current + 1
    elif (final_list[current] > num and sorting == '2') \
            or (final_list[current] < num and sorting == '1'):
        right = current - 1
    else:
        print(current)
        print(list(enumerate(final_list)))
        break

