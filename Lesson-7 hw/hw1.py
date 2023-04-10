# Дана матрица 10х10, заполненная случайными числми(10-1000)
# Напишите программу, которая определяет, сколько в матрице есть 3-знычных чисел, сумма цифр которых равна 5.

counter = 0
import random
matrix = [[random.randint(1, 1000) for i in range(10)] for j in range(10)]
for row in matrix:
    for num in row:
        print(num, end='\t')
        if num >= 100:
            num = str(num)
            num1, num2, num3 = int(num[0]), int(num[1]), int(num[2])
            if num1 + num2 + num3 == 5:
                counter += 1
    print() # Вывод исходной матрицы
print(counter) # Вывод количества 3-значных чисел с суммой цифр внутри равных 5


