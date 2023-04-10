# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран надпись «Good bye!»

summ = 0
maximum = -999999999999999999
minimum = 999999999999999999
while True:
    num1 = int(input('Enter ur number: '))
    if num1 == 7:
        print('Good bye!')
        break
    elif maximum < num1 < minimum:
        maximum = num1
        minimum = num1
        summ += num1
    elif num1 > maximum:
        maximum = num1
        summ += num1
    elif num1 < minimum:
        minimum = num1
        summ += num1
    print(f'ur summ: {summ}')
    print(f'ur maximun: {maximum}')
    print(f'ur minimum: {minimum}')
