# import random
#
# ids = [random.randint(100, 999) for i in range(5)]
# phone_numbers = ['+7' + str(random.randint(1000000000, 9999999999)) for j in range(5)]
# print(ids, phone_numbers)
# while True:
#     command = input('1. Отсортировать по идентификационным кодам\n'
#                     '2. Отсортировать по номерам телефона\n'
#                     '3. Вывести список пользователей с кодами и телефонами\n'
#                     '4. Выход.\n'
#                     'Введите команду: ')
#     if command == '1':
#         for i, values in enumerate(sorted([(id, phone_number) for id, phone_number
#                                            in zip(ids, phone_numbers)], key=lambda x: x[0])):
#             ids[i] = values[0]
#             phone_numbers[i] = values[1]
#     elif command == '2':
#         for i, values in enumerate(sorted([(id, phone_number) for id, phone_number
#                                            in zip(ids, phone_numbers)], key=lambda x: x[1])):
#             ids[i] = values[0]
#             phone_numbers[i] = values[1]
#     elif command == '3':
#         for id, phone_number in zip(ids, phone_numbers):
#             print(f'{id}: {phone_number}')
#     elif command == '4':
#         print('Goodbye!')
#         break


# -------------------------------------------------
# Файлы. Работа с файлами
# Режимы(mode) - r(read)/w(write)/a(add)
# "+" - расширенный режим, в котором можно делать всё
# t(text) - интерпретирует данные с файла, как текст
# b(binary) - интерпретирует данные с файла, как биты

# file = open(file='test.txt', mode='r')
# result = file.read()
# file.close()

# print(file.readline())
# print(file.readlines())
# print(file.read())

# print(file.readable())
# print(file.writable())

# file.write('second one\n')
# file.writelines(['54321\n', '123\n', 'new one'])

# with open('test.txt', 'r') as f, open('new.txt', 'w') as out:
#     out.write(f.read()[::-1])


# 1.

# import re
#
# with open('test.txt', 'r', encoding='utf-8') as in_f:
#     text = in_f.read()
# with open('new.txt', 'w', encoding='utf-8') as out_f:
#     words = re.split('[,.;:!?\s]+', text)
#     print(words)
#     out_f.writelines([f'{word} ' for word in words if len(word) >= 7])


# 2.

# with open('test.txt', 'r', encoding='utf-8') as in_f:
#     text = in_f.readlines()
# with open('new.txt', 'w', encoding='utf-8') as out_f:
#     text = text[::-1]
#     text[0] = text[0] + '\n'
#     text[-1] = text[-1][:-1]
#     out_f.writelines(text)


# 3.

# with open('test.txt', 'r') as f_in, open('new.txt', 'w') as f_out:
#     lines = f_in.readlines()[::-1]
#
#     index = 0
#     for i in range(len(lines)):
#         if ',' not in lines[i]:
#             index = i
#             break
#
#     lines.insert(index, '\n' + '*'*12 if index == 0 else '*'*12 + '\n')
#     f_out.writelines(lines[::-1])


# 4.

# import re
#
# with open('test.txt', 'r', encoding='utf-8') as f_in:
#     words = re.split('[,.\s!?:;]+', f_in.read())
#     symbol = input('Введите символ: ')
#     print(len([word for word in words if word.lower().startswith(symbol.lower())]))


# 5.

# with open('test.txt', 'r', encoding='utf-8') as f_in:
#     text = f_in.read()
#     print('Символы: ', len(text))
#     print('Строки: ', text.count('\n') + 1)
