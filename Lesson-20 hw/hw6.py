# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется пользователем.
import re

old_word = input('Введите слово для замены ')
new_word = input('Введите слово, на которое произведётся замена: ')

with open(file="file1.txt", mode="r", encoding="utf-8") as my_file1, open(file="file2.txt", mode="w", encoding="utf-8")\
        as my_file2:
    my_text = my_file1.read()
    replaced_text = re.sub(old_word, new_word, my_text, flags=re.IGNORECASE)
    my_file2.write(replaced_text)