# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»

while True:
    num1 = int(input('Enter ur number: '))
    if 7 > num1 > 0 or num1 > 7:
        print('Number is positive')
    elif num1 < 0:
        print('Number is negative')
    elif num1 == 0:
        print('Number is equal to zero')
    else:
        print('Good bye!')
        break
