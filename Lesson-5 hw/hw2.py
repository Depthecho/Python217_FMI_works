# Пользователь вводит с клавиатуры некоторый текст, после чего пользователь вводит список зарезервированных слов.
# Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. Вывести на экран измененный
# текст.

my_string, word1, word2, word3 = input('Введите ваш текст: '), input('Введите 3 ваших слова: '), input(), input()
my_string2 = ''
string_words = my_string.split()
for i in string_words:
    if i == word1 or i == word2 or i == word3:
        i = i.title()
    my_string2 += i +' '
print(my_string2)
# print(string_words)