# Подсчитать количество целых чисел в диапазоне от 100 до 9999 у которых все цифры разные.
summ1 = 0
summ2 = 0
for a in range(100, 10000):
    num1 = (a // 1000)
    num2 = (a // 100) % 10
    num3 = (a % 10) // 10
    num4 = a % 10
    if a <= 1000:
        if num2 != num3 and num2 != num4 and num3 != num4:
            summ1 += 1
    if a >= 1000:
        if num1 != num2 and num1 != num3 and num1 != num4 and num2 != num1 and num2 != num3 and num2 != num4 and num3 != num4:
            summ2 += 1
print("Количество разных целых чисел в диапазоне от 100 до 9999:", summ1 + summ2)
