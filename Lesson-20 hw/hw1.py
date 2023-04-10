# Дано два текстовых файла. Выяснить, совпадают ли их строки. Если нет, то вывести несовпадающую строку из каждого
# файла.

with open(file="file1.txt", mode="r", encoding="utf-8") as my_file1, open(file="file2.txt", mode="r", encoding="utf-8")\
        as my_file2:
    file1_lines = my_file1.readlines()
    file2_lines = my_file2.readlines()

    i = 0
    for line1, line2 in zip(file1_lines, file2_lines):
        i += 1
        if line1 != line2:
            print(f"Строка из 1-го файла: {line1}")
            print(f"Строка из 2-го файла: {line2}")