# Напишите функцию make_counter, которая принимает число n в качестве аргумента и возвращает замыкание, которое
# можно использовать для обратно отсчёта от n до 0.

def make_counter(n):
    def counter():
        nonlocal n
        if n >= 0:
            print(n)
            n -= 1
        else:
            print('Error: Counter has reached 0')
        return n
    return counter


c = make_counter(3)
c()
c()
c()
c()
c()