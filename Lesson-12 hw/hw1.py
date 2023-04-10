# Напишите лямбда-функцию, которая принимает строку и возвращает копию строку с удалёнными гласными.

my_vowels = ['a', 'e', 'y', 'u', 'o', 'i', 'а', 'у', 'е', 'о', 'ы', 'ё', 'я', 'и', 'ю', 'э']
my_string = input('Придумайте вашу строку: ')

my_string2 = lambda row: ''.join([i for i in row if i.lower() not in my_vowels])
print(my_string2(my_string))


