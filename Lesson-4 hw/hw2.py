# Подсчитать количество целых чисел в диапазоне от 100 до 999 у которых есть две одинаковые цифры.
summ = 0
for i in range(100, 1000):
    num1 = int(i // 100)
    num2 = int(i / 100 // 10)
    num3 = int(i % 10)
    if num1 == num2 or num2 == num3 or num1 == num3:
        summ += 1
print(summ)
