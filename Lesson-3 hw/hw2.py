# П ользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
# числа в этом диапазоне. Нужно вывести на экран:
# Все числа диапазона;
# Все числа диапазона в убывающем порядке;
# Все числа, кратные 7;
# Количество чисел, кратных 5.

num1, num2 = int(input('Введите ваше первое число: ')), int(input('Введите ваше второе число: '))
sub = 1
summ = 0
summ_multi5 = 0
numbers_multi7 = 1
numbers_multi5 = 0
if num2 > num1:
    num1, num2 = num2, num1
while num2 <= num1:
    print(f'{sub} число в правильном порядке: {num2}')
    print(f'{sub} число в обратном порядке: {num1 - sub}')
    if num2 % 7 == 0:
        print(f'{numbers_multi7} число, кратное 7: {num2}')
        numbers_multi7 += 1
    elif num2 % 5 == 0:
        summ_multi5 += 1
    num2 += 1
    sub += 1
print(f'Количество чисел, кратных 5: {summ_multi5}')

# Других идей у меня, чтобы вывести каждое решение отдельно, у меня не было
