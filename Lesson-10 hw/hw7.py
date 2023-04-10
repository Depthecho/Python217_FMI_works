# Напишите функцию, которая проверяет является ли число палиндромом. Число передаётся в качестве пара-метра. \
# Если число палиндром нужно вернуть из функции true, иначе false.

num = int(input("Введите число: "))


def get_palindrome(num: int) -> bool:
    copy_num = num
    num2 = 0
    while (num > 0):
        num3 = num % 10
        num2 = num2 * 10 + num3
        num = num // 10
    if copy_num == num2:
        return True
    else:
        return False

get_palindrome(num)
