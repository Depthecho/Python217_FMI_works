# Напиши лямбда-функцию, которая принимает список строкк и возвращет новый список, содержащий только строки,
# являющиеся палиндромами

n = int(input('Введите количество строк в списке: '))
i = 1
my_list = []
multi = 1

while i <= n:
    my_strings = input(f'Введите ваше {i} число: ')
    my_list.append(my_strings)
    i += 1

my_list2 = lambda lst: list(filter(lambda x: x == x[::-1], lst))
print(my_list2(my_list))

