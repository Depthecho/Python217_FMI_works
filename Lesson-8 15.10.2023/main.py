# 1.

# 1 Solution

# strs = ["alic3", "bob", "3", "4", "00000"]
# max_value = len(strs[0])
#
# for word in strs:
#     if word.isdigit():
#         if int(word) > max_value:
#             max_value = int(word)
#     else:
#         if len(word) > max_value:
#             max_value = len(word)
# print(max_value)


# 2 Solution

# strs = ["alic3", "bob", "3", "4", "00000"]
# max_value = len(strs[0])
# for string in strs:
#     max_value = max(max_value, int(string)) \
#                 if string.isdigit() else \
#                 max(max_value, len(string))
#
# print(max_value)


# 3 Solution
# strs = ["alic3", "bob", "3", "4", "00000"]
# print(max([int(x) if x.isdigit() else len(x) for x in strs]))
#     максимум(список(значение числа, если строка из цифр иначе
#                     длину строки для каждой строки в списке strs))


# 2.

# 1 Solution

# words = ["mass", "as", "hero", "superhero"]
# sub_strs = []
# for string in words:
#     count = 0
#     for another_string in words:
#         if string in another_string:
#             count += 1
#     if count > 1:
#         sub_strs.append(string)
#
# print(sub_strs)


# 2 Solution

# words = ["mass", "as", "hero", "superhero"]
# all_strings = ' '.join(words)
# sub_strs = [string for string in words
#             if all_strings.count(string) > 1]
#
# print(sub_strs)


# 3.

# 1 Solution

# event1 = ["02:00", "03:00"]
# event2 = ["01:15", "02:00"]
# start_event1 = 60 * int(event1[0][0:2]) + \
#                     int(event1[0][3:])
# finish_event1 = 60 * int(event1[1][0:2]) + \
#                      int(event1[1][3:])
# start_event2 = 60 * int(event2[0][0:2]) + \
#                     int(event2[0][3:])
# finish_event2 = 60 * int(event2[1][0:2]) + \
#                      int(event2[1][3:])
#
# if start_event1 <= start_event2 <= finish_event1 \
#  or start_event2 <= start_event1 <= finish_event2:
#     print(True)
# else:
#     print(False)


# print('01' < '02')  # 4849 < 4850 => True
# print('03' < '02')  # 4851 < 4850 => False
# print('01:15' < '01:10')
# print('01:05' < '01:10')  # 4849584853 <
#                           # 4849584948


# 2 Solution
# event1 = ["02:00", "03:00"]
# event2 = ["01:15", "02:00"]
# print(event1[0] <= event2[1] and event2[0] <= event1[1])


# 4.

# 1 Solution

# import random
#
# heights = [random.randint(1, 5) for i in range(10)]
# count = 0
# k = sorted(heights)
# for i in range(10):
#     if heights[i] != k[i]:
#         count += 1
# print(heights)
# print(k)
# print(count)


# zip(list1, list2) => возвращает генератор, который
# позволяет итерироваться по n элементам из
# n списков в виде кортежей.
# Пример
# for i, j in zip([1,2,3], ['a','b','c']):
#     print(i, j)
# <<< 1 a
# <<< 2 b
# <<< 3 c


# 2 Solution

# import random
#
# heights = [random.randint(1, 5) for i in range(10)]
# print(sum([h1 != h2 for h1, h2 in zip(heights, sorted(heights))]))


# 5.


# import random
#
# nums = [random.randint(1, 20) for i in range(5)]
# print(nums)
#
# for i in range(len(nums)):
#     nums.append(int(str(nums[i])[::-1]))
# print('После добавления перевернутых копий:')
# print(nums)
#
# unique_nums = []
# for num in nums:
#     if num not in unique_nums:
#         unique_nums.append(num)
#
# print('Уникальные элементы:')
# print(unique_nums)
# print(len(unique_nums))


# 6.

# import random
#
# nums = [random.randint(1, 10) for i in range(10)]
# print(nums)
# print((nums.pop(nums.index(max(nums))) - 1) * (max(nums) - 1))


