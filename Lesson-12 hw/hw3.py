# Напишите лямбду-функцию, которая принимает список целых чисел и возвращает их произведение.
from functools import reduce

n = int(input('Введите количество чисел в списке: '))
i = 1
my_list = []
multi = 1

while i <= n:
    num = int(input(f'Введите ваше {i} число: '))
    my_list.append(num)
    i += 1

my_multi = lambda numbers: reduce(lambda x, y: x*y, numbers)
print(my_multi(my_list))

# Задание просто взрыв мозга))
