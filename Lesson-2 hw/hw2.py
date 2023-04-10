num1, num2, num3, condition=int(input('Введите 3 ваших числа: ')), int(input()), int(input()), input('Введите название операции ( min, max or middle): ')
if condition=="min":
    if num1< num2 and num1<num3:
        print(num1)
    elif num2<num1 and num2<num3:
        print(num3)
    else:
        print(num3)
elif condition=="max":
    if num1> num2 and num1>num3:
        print(num1)
    elif num2>num1 and num2>num3:
        print(num3)
    else:
        print(num3)
elif condition=="middle":
    print((num1+num2+num3)/2)
else:
    print('Неверное название операции')