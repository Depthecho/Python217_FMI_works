meters, condition=int(input('Введите ваше количество метров: ')),input('Введите единицы измерения, в которую хотите преобразоваать из вашеей единицы измерения (miles, inches, yards): \n')
if condition=="miles":
    print(f'{meters*0.000621} милей')
elif condition=="inches":
    print(f'{meters*39.37008} дюймов ')
elif condition=="yards":
    print(f'{meters * 1.093613} ярдов ')
else:
    print('Неверная операция')