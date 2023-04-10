# Напишите функцию-ограничитель, которая принимает функцию в качестве аргумента и возвращает замыкание, ограничивающее
# частоту, с которой функция может быть вызвана. Замыкание должно принимать любое количество аргументов, вызвать функцию
# с этими аргументами, если с момента последнего вызова прошло доастаточно времени, и возвращать результат.
import time


def say_hello(name):
    print(f'Hello {name}!')


def throttle(func, num):
    start = time.time()
    called = False
    timer = num

    def closure(*args):
        nonlocal called, num
        if not called:
            func(*args)
            print('do nothing...')
            called = True
        else:
            end = time.time()
            total_time = end - start
            return func(*args) if total_time >= timer else ...

    return closure


throttled_hello = throttle(say_hello, 2)
throttled_hello('Alice')
time.sleep(1)
throttled_hello('Bob')
time.sleep(2)
throttled_hello('Charlie')
