# Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой файл.

with open(file="file1.txt", mode="r", encoding="utf-8") as my_file1, open(file="file2.txt", mode="w", encoding="utf-8")\
        as my_file2:
    lines = my_file1.readlines()

    if len(lines) > 0:
        lines.pop()

    my_file2.writelines(lines)