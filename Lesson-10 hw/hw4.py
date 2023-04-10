# Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.

import random

n = 5
my_list = [random.randint(1, 100) for i in range(n)]
print(my_list)


def get_minimum(a: list) -> int:
    my_minimum = a[0]
    for i in a:
        if i < my_minimum:
            minimum = i
    return my_minimum


get_minimum(my_list)

