num1=int(input('Введите порядковый номер месяца: '))
month30=30
month31=31
month28=28
if num1==1 or num1==3 or num1==5 or num1== 7 or num1== 8 or num1== 10 or num1== 12:
    print(f'{month31} день')
elif num1== 4 or num1== 6 or num1== 9 or num1== 11:
    print(f'{month30} дней')
else:
    print(f'{month28} дней')