# Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра.
# Из функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.

num = int(input("Введите число: "))


def get_number(num1: int) -> int:
    num2 = 0
    counter = 0
    for i in range(len(str(num1))):
        num2 = num1 % 10
        num1 - num2
        counter += 1
    print(counter)
    return counter


get_number(num)
