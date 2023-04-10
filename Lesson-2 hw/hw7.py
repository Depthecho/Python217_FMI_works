num1, num2=int(input('Введите 2 числа: ')), int(input())
if num1==num2:
    print('Числаа равны')
else:
    if num1 > num2:
        num1, num2 = num1, num2
    elif num1 < num2:
        num1, num2 = num2, num1
    print(f'{num2}, {num1}')