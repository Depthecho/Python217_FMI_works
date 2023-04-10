# Есть некоторый текст. Посчитайте в этом тексте ко-личество предложений и выведите на экран полученный результат.

my_string = input('Введите ваш текст: ')
znak1 = my_string.count('.')
znak2 = my_string.count('!')
znak3 = my_string.count('?')
print(f'Количество предложений: {znak1+znak2+znak3}')