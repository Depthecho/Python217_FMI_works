# Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.

num1, num2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))
my_list = []


def even_order(num1: int, num2: int) -> int:
    def reverse_if_need(num1: int, num2: int) -> tuple[int, int]:
        if num1 > num2:
            num1, num2 = num2, num1
            return num1, num2
        else:
            return num2, num1

    reverse_if_need(num1, num2)

    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            my_list.append(i)
    print(my_list)
    return my_list


even_order(num1, num2)

