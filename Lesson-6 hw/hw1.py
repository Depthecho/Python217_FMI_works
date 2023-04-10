# Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12.Необходимо вывести на экран результат
# выражения. В нашем примере это 35. Арифметическое выражение может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/

spisok = input('Введите ваше выражение: ')
symbols = spisok.split()
symbols[0] = int(symbols[0])
symbols[2] = int(symbols[2])
if symbols[1] == '+':
    print(f'{symbols[0]} + {symbols[2]} = {symbols[0] + symbols[2]}')
elif symbols[1] == '-':
    print(f'{symbols[0]} - {symbols[2]} = {symbols[0] - symbols[2]}')
elif symbols[1] == '*':
    print(f'{symbols[0]} * {symbols[2]} = {symbols[0] * symbols[2]}')
elif symbols[1] == '/':
    if symbols[2] == 0:
        print('Функция деления невозможна')
    else:
        print(f'{symbols[0]} / {symbols[2]} = {symbols[0] / symbols[2]}')
