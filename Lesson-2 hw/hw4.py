num = int(input('Введите день недели по счёту от 1 до 7: '))
day = ''
if 1 <= num <= 7:
    if num == 1:
        day = 'Понедельник'
    elif num == 2:
        day = "Вторник"
    elif num == 3:
        day = "Среда"
    elif num == 4:
        day = "Четверг"
    elif num == 5:
        day = "Пятница"
    elif num == 6:
        day = "Суббота"
    else:
        day = "Воскресенье"
    print(day)
else:
    print('Невернаая операция')
