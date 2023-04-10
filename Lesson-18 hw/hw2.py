# Написать программу «справочник». Создать два списка целых. Один список хранит идентификационные коды,
# второй — телефонные номера. Реализовать меню для пользователя:


books = ["Война и мир", "Мастер и Маргарита", "Анна Каренина", "Отцы и дети", "Преступление и наказание"]
years = [1869, 1966, 1877, 1862, 1866]
for i in range(len(books)):
    print(f"{books[i]}, {years[i]}")

while True:
    print("Меню:")
    print("1. Отсортировать по названию книг")
    print("2. Отсортировать по годам выпуска")
    print("3. Вывести список книг с названиями и годами выпуска")
    print("4. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        sorted_books = sorted(books)
        print("Список книг, отсортированный по названию:")
        for i in range(len(sorted_books)):
            print(f"{sorted_books[i]}, {years[books.index(sorted_books[i])]}")
    elif choice == "2":
        sorted_years = sorted(years)
        print("Список книг, отсортированный по годам выпуска:")
        for i in range(len(sorted_years)):
            print(f"{books[years.index(sorted_years[i])]}, {sorted_years[i]}")
    elif choice == "3":
        print("Список книг:")
        for i in range(len(books)):
            print(f"{books[i]}, {years[i]}")
    elif choice == "4":
        print('Программа приостановлена')
        break
    else:
        print("Некорректный выбор, попробуйте еще раз")
