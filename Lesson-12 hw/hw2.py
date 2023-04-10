# Напишите лямбду-функцию, которая принимает строку и возвращает True, если она содержит только буквы алфавита,
# и False в противном случе.

my_string = input('Придумайте вашу строку: ')

my_string2 = lambda i: [True if i.isalpha() else False]
print(my_string2(my_string))


