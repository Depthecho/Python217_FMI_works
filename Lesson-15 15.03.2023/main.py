# Closure - Замыкание - ситуация, при которой происходит
# обращение к данным, контекста которых не существует
# Иногда замыканием называют непосредственно функцию,
# которую делает наша функция, т.е. функцию power

# def make_func(num):
#     def power(pow):
#         return num ** pow
#
#     return power
#
#
# power_of_five = make_func(5)
# power_of_two = make_func(2)
# print(power_of_five(3))
# print(power_of_two(10))

# 1.
# Напишите функцию, которая создаёт другую функцию.
# Эта созданная функция должна изменять вывод данных
# в зависимости от символа, который был передан в первую
# функцию.

# Пример:
# pretty_stars = func('*')
#
# pretty_stars('Name')
# >>> '*Name*'

# pretty_dollars = func('$')
#
# pretty_dollars('Name')
# >>> '$Name$'

# def func(symbol):
#     def pretty(word):
#         return f'{symbol}{word}{symbol}'
#     return pretty
#
#
# pretty_stars = func('*')
# print(pretty_stars('Егор'))

# num = 5
# def add_one():
#     global num
#     num = 3
#     return num
#
# print(add_one())
# print(num)


# def foo():
#     num = 1
#     def goo():
#         nonlocal num
#         num += 2
#         print(num)  # local -> nonlocal -> global
#     goo()
#
# foo()

# 2.
# Напишите функцию счетчик, которая возвращает
# замыкание, отслеживающее, сколько раз оно
# было вызвано. Замыкание не должно принимать
# аргументов и возвращать целое число,
# представляющее количество раз, когда оно
# было вызвано.

# Пример использования:
# >>> c = counter()
# >>> c()
# 1
# >>> c()
# 2
# >>> c()
# 3

# def counter():
#     count = 0
#     def c():
#         nonlocal count
#         count += 1
#         return count
#     return c
#
# c = counter()
# print(c())
# print(c())
# print(c())
# print(c())


# 3.
# Напишите функцию нахождения среднего,
# которая возвращает замыкание.
# Замыкание должно принимать один аргумент,
# представляющий число в последовательности,
# и возвращать текущее среднее значение.

# Пример использования:
# >>> avg = average()
# >>> avg(10)
# 10.0
# >>> avg(20)
# 15.0
# >>> avg(30)
# 20.0

# def closure():
#     total = 0
#     count = 0
#     def inner(number):
#         nonlocal total, count
#         total += number
#         count += 1
#         return total / count
#
#     return inner
#
#
# avg = closure()
# print(avg(10))
# print(avg(20))
# print(avg(30))


# 4.
# Напишите функцию password_protected, которая
# принимает пароль в качестве аргумента и
# возвращает замыкание, которое можно
# использовать для защиты доступа к
# конфиденциальной функции. Закрытие должно
# принимать один аргумент, представляющий
# пароль,
# и возвращать результат чувствительной
# функции, если пароль правильный,
# и сообщение об ошибке в противном случае.

# Пример использования:
# >>> def sensitive_function():
# ...     return "You have accessed a sensitive function!"
# ...
# >>> protected_function = password_protected("abc123")
# >>> protected_function("abc123")
# "You have accessed a sensitive function!"
# >>> protected_function("incorrect_password")
# "Error: incorrect password"


# def sensitive_function():
#     return "You have accessed a sensitive function!"
#
#
# def password_protected(password):
#     def inner(pw):
#         if pw == password:
#             return sensitive_function()
#         else:
#             return "Error: incorrect password"
#     return inner
#
#
# protected_function = password_protected("abc123")
# print(protected_function("abc123"))
# print(protected_function("321"))
# print(protected_function("abc123"))


# 5.

# Напишите функцию memoize, которая принимает
# функцию в качестве аргумента и возвращает
# замыкание, кэширующее результаты функции.
# Замыкание должно принимать любое количество
# аргументов и возвращать кэшированный
# результат, если те же аргументы были
# переданы ранее, или вычислять и кэшировать
# результат в противном случае.

# Пример использования:

# >>> def slow_add(x, y):
# ...     print("Computing...")
# ...     return x + y
# ...
# >>> fast_add = memoize(slow_add)
# >>> fast_add(1, 2)
# Computing...
# 3
# >>> fast_add(1, 2)
# 3
# >>> fast_add(2, 3)
# Computing...
# 5

# def slow_add(x, y):
#     print("Computing...")
#     return x + y
#
#
# def memoize(func):
#     cache = {}
#
#     def closure(*args, **kwargs):
#         nonlocal cache
#         if (args, *kwargs.items()) not in cache.keys():
#             cache[(args, *kwargs.items())] = func(*args, **kwargs)
#         return cache[(args, *kwargs.items())]
#
#     return closure
#
#
# fast_add = memoize(slow_add)
#
# print(fast_add(2, 3))


# 6.

# Напишите функцию, которая принимает функцию в
# качестве аргумента и возвращает замыкание,
# которое выполняет функцию только один раз,
# независимо от того, сколько раз замыкание
# вызывается. Пример использования:

# def say_hello():
#     print("Hello!")
#
# once_hello = once(say_hello)
# once_hello() # Выводит "Hello!"
# once_hello() # Ничего не делает

# def say_hello():
#     print("Hello!")
#
#
# def once(func):
#     runned = False
#
#     def closure():
#         nonlocal runned
#         if not runned:
#             runned = True
#             return func()
#
#     return closure
#
#
# once_hello = once(say_hello)
# once_hello()
# once_hello()
# once_hello()
