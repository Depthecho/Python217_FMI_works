# Напишите информационную систему «Сотрудники». Программа должна обеспечивать ввод данных, редакти-рование данных
# сотрудника, удаление сотрудника, поиск сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного
# возраста, или фамилия которых начинается на указанную букву. Организуйте возможность сохранения найденной информации
# в файл. Также весь список сотрудников сохраняется в файл (при выходе из программы — автоматически, в процессе
# исполнения программы — по команде пользователя). При старте программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

workers = []


def add_worker():
    name = input("Введите имя работника: ")
    surname = input("Введите фамилию раюотника: ")
    age = input("Введите возраст работника: ")
    salary = input("Введите зарплату работника: ")
    workers.append({'first_name': name, 'last_name': surname, 'age': age, 'salary': salary})
    print("Данные работника успешно добавлены.")


def remove_worker():
    last_name = input("Введите фамилию работника: ")
    for worker in workers:
        if worker['last_name'] == last_name:
            workers.remove(worker)
            print("Данные о работнике успешно удалены.")
            return


def edit_worker():
    surname = input("Введите фамилию работника для редактирования его данных: ")
    for worker in workers:
        if worker['last_name'] == surname:
            worker['first_name'] = input("Введите новое имя: ")
            worker['age'] = input("Введите новый возраст: ")
            worker['salary'] = input("Введите новую зарплату: ")
            print("Данные о работнике успешно изменены.")
            return


def find_worker_by_lastname():
    last_name = input("Введите фамилию работника для поиска: ")
    for worker in workers:
        if worker['last_name'] == last_name:
            print(f"Имя: {worker['first_name']}\nВозраст: {worker['age']}\nЗарплата: {worker['salary']}")
            return


def find_worker_by_age():
    age = input("Введите возраст работника: ")
    for worker in workers:
        if worker['age'] == age:
            print(f"Имя: {worker['first_name']}\nФамилия: {worker['last_name']}\nЗарплата: {worker['salary']}")


def find_worker_by_initial():
    initial = input("Введите первую букву фамилии работника: ")
    for worker in workers:
        if worker['last_name'].startswith(initial):
            print(
                f"Имя: {worker['first_name']}\nФамилия: {worker['last_name']}\nВозраст: {worker['age']}\nЗарплата: {worker['salary']}")


def show_all_workers():
    for worker in workers:
        print(
            f"Имя: {worker['first_name']}\nФамилия: {worker['last_name']}\nВозраст: {worker['age']}\nЗарплата: {worker['salary']}\n ================================================================")


def save_workers_to_file():
    with open(file="workers.txt", mode="a", encoding="utf-8") as workers_file:
        for worker in workers:
            workers_file.write(f"{worker['first_name']}, {worker['last_name']}, {worker['age']}, {worker['salary']}\n")


def load_workers_from_file():
    with open(file="workers.txt", mode="r", encoding="utf-8") as workers_file:
        for line in workers_file:
            first_name, last_name, age, salary = line.strip().split(",")
            workers.append({'first_name': first_name, 'last_name': last_name, 'age': age, 'salary': salary})


def workers_prog():
    load_workers_from_file()

    while True:
        print("Меню работников:")
        print("1. Добавить данные работника.")
        print("2. Удалить данные работника.")
        print("3. Редактировать данные работника.")
        print("4. Поиск работника по фамилии.")
        print("5. Поиск работника по возрасту.")
        print("6. Поиск работника по инициалам.")
        print("7. Показ всех работников.")
        print("8. Загрузить данные о работнике в файл")
        print("9. Exit")
        choice = input("Ваш выбор: ")

        if choice == "1":
            add_worker()
        elif choice == "2":
            remove_worker()
        elif choice == "3":
            edit_worker()
        elif choice == "4":
            find_worker_by_lastname()
        elif choice == "5":
            find_worker_by_age()
        elif choice == "6":
            find_worker_by_initial()
        elif choice == "7":
            show_all_workers()
        elif choice == "8":
            save_workers_to_file()
        elif choice == "9":
            with open(file="workers.txt", mode="w", encoding="utf-8") as workers_file:
                for worker in workers:
                    workers_file.write(
                        f"{worker['first_name']}, {worker['last_name']}, {worker['age']}, {worker['salary']}\n")
            break
        else:
            print('Вы ввели что-то неправильно...')


workers_prog()
# Только единственный минус, я не могу понять, почему 4,5 и 6 команды не работают с уже имеющимися в файле работниками,
# Вроде всё правильно написал
