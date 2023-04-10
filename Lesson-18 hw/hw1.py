# Написать программу «справочник». Создать два списка целых. Один список хранит идентификационные коды,
# второй — телефонные номера. Реализовать меню для пользователя

codes = [1234, 5678, 9012, 3456]
phones = ['+79123456789', '+79234567890', '+79091234567', '+79081234567']
for i in range(len(codes)):
    print(f"{codes[i]}: {phones[i]}")


while True:
    print("Меню:\n"
          "1 - Отсортировать по идентификационным кодам\n"
          "2 - Отсортировать по номерам телефона\n"
          "3 - Вывести список пользователей с кодами и телефонами\n"
          "4 - Выход\n")
    choice = input("Выберите действие: ")

    if choice == '1':
        for i in range(len(codes)):
            for j in range(len(codes) - 1 - i):
                if codes[j] > codes[j+1]:
                    codes[j], codes[j+1] = codes[j+1], codes[j]
                    phones[j], phones[j+1] = phones[j+1], phones[j]
        print("Список отсортирован по идентификационным кодам")
        for i in range(len(codes)):
            print(f"{codes[i]}: {phones[i]}")
    elif choice == '2':
        for i in range(len(phones)):
            for j in range(len(phones) - 1 - i):
                if phones[j] > phones[j+1]:
                    phones[j], phones[j+1] = phones[j+1], phones[j]
                    codes[j], codes[j+1] = codes[j+1], codes[j]
        print("Список отсортирован по номерам телефона")
        for i in range(len(codes)):
            print(f"{codes[i]}: {phones[i]}")
    elif choice == '3':
        print("Список пользователей:")
        for i in range(len(codes)):
            print(f"Код: {codes[i]}, Телефон: {phones[i]}")
    elif choice == '4':
        print('Программа приостановлена')
        break
    else:
        print("Неверный ввод, попробуйте еще раз")