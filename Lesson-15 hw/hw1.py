#  Напишите функцию repeat_until, которая принимает функцию f и предикат p в качестве аргументов и возвращают замыкание,
#  которое повторно применяет f к своему собственному выводу, пока p не вернёт True.

def half(x):
    return x // 2


def is_even(x):
    return x % 2 == 0


def repeat_until(f, p):
    statement = False
    counter = 0

    def closure(num):
        nonlocal statement, counter
        while statement is not True:
            number = f(num)
            num = number
            statement = p(num)
            counter += 1
        print(num)
        return

    return closure


repeat_until_half_even = repeat_until(half, is_even)
repeat_until_half_even(19)