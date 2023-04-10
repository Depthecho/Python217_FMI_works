# Напишите лямбда-функцию, которя принимает число и возвращает True, если оно является простым, и False в противном
# случае

num = int(input('Введите число: '))

prime_num = lambda x: [False if [x for x in range(2, (num//2)+1) if num % x == 0] else True]
print(prime_num(num))
