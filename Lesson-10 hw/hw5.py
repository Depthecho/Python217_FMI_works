# Напишите функцию, которая возвращает произве-дение чисел в указанном диапазоне. Границы диапазона передаются
# в качестве параметров. Если границы диапа-зона перепутаны (например, 5 — верхняя граница, 25 — нижняя граница),
# их нужно поменять местами.

num1 = int(input('Введите начало диапазона: '))
num2 = int(input('Введите конец диапазона: '))


def get_multi_order(num1: int, num2: int) -> int:
    multi = 1

    def reverse_if_need(num1: int, num2: int) -> int:
        if num1 > num2:
            num1, num2 = num2, num1
            return num1, num2
        else:
            return num1, num2

    num1, num2 = reverse_if_need(num1, num2)

    for i in range(num1, num2 + 1):
        multi *= i
    print(multi)
    return multi


get_multi_order(num1, num2)
