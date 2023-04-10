# Написать программу, реализующую сортировку списка методом усовершенствованной сортировки пузырьковым методом.
# Усовершенствование состоит в том, чтобы ана-лизировать количество перестановок на каждом шагу, если это количество
# равно нулю, то продолжать сортировку нет смысла — список отсортирован.

import random

my_list = [random.randint(0,100) for i in range(10)]
print(my_list)


def bubble_sort(lst):
    length = len(lst)
    while length > 1:
        new_length = 0
        for i in range(1, length):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                new_length = i
        length = new_length
        if length == 0:
            break
    return lst


print(bubble_sort(my_list))