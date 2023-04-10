# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция принимает
# в качестве параметров: длину стороны ква-драта, символ и переменную логического типа:
#  если она равна True, квадрат заполненный;
#  если False, квадрат пустой.

length = int(input("Введите длину стороны квадрата: "))
symbol = input("Введите символ: ")
answer = input('Введите True или False: ')
my_string = ' '


def get_square(length: int, symbol: str, answer: bool):
    if answer == 'True':
        for i in range(length):
            print(f'{symbol * length}')

    elif answer == 'False':
        for i in range(length):
            if i == 0 or i == length - 1:
                print(f'{symbol * length}')
            else:
                print(f'{symbol} {my_string * (length - 2)} {symbol}')
    else:
        print('Неверная команда!')


get_square(length, symbol, answer)
