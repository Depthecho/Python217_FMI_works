# Дан текстовый файл. Найти длину самой длинной строки.

with open(file="file1.txt",mode="r", encoding="utf-8") as my_file:
    max_length = 0
    for line in my_file:
        line_length = len(line.rstrip("\n"))
        if line_length > max_length:
            max_length = line_length

print(f'Длинна самой длинной строки: {max_length}')
