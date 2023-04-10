# Написать рекурсивную функцию нахождения наи-большего общего делителя двух целых чисел.

num1, num2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))
my_divider_list = list()  # Создание листа для занесения туда делителей.


def get_divider(num1: int, num2: int, counter=1) -> int:
    # Основная функция для подсчёта делителей.
    def reverse_if_need(num1: int, num2: int) -> int:
        # Функция для переворота значений.
        if num1 > num2:
            num1, num2 = num2, num1
            return num1, num2
        else:
            return num1, num2

    num1, num2 = reverse_if_need(num1, num2)

    while counter <= num1:
        if num1 % counter == 0 and num2 % counter == 0:
            my_divider_list.append(counter)
        return get_divider(num1, num2, counter + 1)
    return my_divider_list[-1]


print(get_divider(num1, num2, counter=1))
