# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы

num1, num2 = int(input('Введите начало диапазон: ')), int(input('Введите конец диапазона: '))
a = 1
b = 1
c = 1
summ_even = 0
summ_even_middle = 0
summ_odd = 0
summ_odd_middle = 0
summ_multiples9 = 0
summ_multiples9_middle = 0
if num2 > num1:
    num1, num2 = num2, num1
while num2 <= num1:
    if num2 % 9 == 0:
        summ_multiples9 += num2
        summ_even_middle = summ_multiples9 / c
        c += 1
    elif num2 % 2 != 0:
        summ_odd += num2
        summ_odd_middle = summ_odd / a
        a += 1
    elif num2 % 2 == 0:
        summ_even += num2
        summ_even_middle = summ_even / b
        b += 1
    num2 += 1
print(f'Сумма чётных: {summ_even}')
print(f'Среднее арифметическое чётных: {summ_even_middle}')
print(f'Сумма нечётных: {summ_odd}')
print(f'Среднее арифметическое нечётных: {summ_odd_middle}')
print(f'Сумма кратных 9: {summ_multiples9}')
print(f'Среднее арифметическое кратных 9: {summ_multiples9}')
