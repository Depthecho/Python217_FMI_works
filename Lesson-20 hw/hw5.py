# Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.

word = input("Введите слово для счёта: ")

with open(file="file1.txt", mode="r", encoding="utf-8") as my_file:
    count = 0
    for line in my_file:
        words = line.split()
        for w in words:
            if w == word or w.lower() == word.lower():
                count += 1

print(f"Заданное вам слово встретилось {count} раз(а)")
