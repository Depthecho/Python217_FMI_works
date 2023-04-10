# Необходимо отсортировать первые две трети списка в порядке возрастания, если среднее арифметическое всех элементов
# больше нуля; иначе — лишь первую треть. Остальную часть списка не сортировать, а расположить в обратном порядке.

import random

my_list = [random.randint(-10, 10) for i in range(10)]
print(my_list)


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def sort_list(lst):
    n = len(lst)
    avg = sum(lst) / n
    print(avg)
    if avg > 0:
        bubble_sort(lst[:2*n//3])
        lst[2*n//3:] = lst[2*n//3:][::-1]
        return lst
    else:
        bubble_sort(lst[:n//3])
        lst[n//3:][::-1]
        return lst


print(sort_list(my_list))