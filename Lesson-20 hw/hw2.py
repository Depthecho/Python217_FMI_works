# Дан текстовый файл. Необходимо создать новый файл и записать в него следующую статистику по исходному файлу:
# Количество символов;
# Количество строк;
# Количество гласных букв;
# Количество согласных букв;
# Количество цифр.

vowels = "aeiouyAEIOUY"
consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
digits = "0123456789"

with open(file="file1.txt" ,mode="r", encoding="utf-8") as my_file1, open(file="file2.txt", mode="a", encoding="utf-8") \
        as my_file2:
    my_text = my_file1.read()
    count_vow, count_con, count_dig = 0, 0, 0

    for count_vow, count_con, count_dig in my_text:
        if count_vow in vowels:
            count_vow += 1
        elif count_con in consonants:
            count_con += 1
        elif count_dig in digits:
            count_dig += 1

    count_chars = len(my_text)
    count_lines = my_text.count("/n")

    my_file2.write(f"Количество букв: {count_chars}\n")
    my_file2.write(f"Количество строк: {count_lines}\n")
    my_file2.write(f"Количество гласных: {count_vow}\n")
    my_file2.write(f"Количество согласных: {count_con}\n")
    my_file2.write(f"Количество цифр: {count_dig}\n")

