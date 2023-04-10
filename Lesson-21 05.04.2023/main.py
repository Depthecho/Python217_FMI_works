# Дан текстовый файл. Необходимо создать новый файл, убрав из него все неприемлемые слова. Список неприемлемых
# слов находится в другом текстовом файле
#
# with open('text.txt', 'r', encoding='utf-8') as my_text, open('words.txt', 'r', encoding='utf-8') as bad_words:
#     text = my_text.read()
#     bad_word = bad_words.read().split()
#
#     for i in bad_word:
#         text = text.replace(i, "")
#
# with open('text2.txt', 'w', encoding='utf-8') as my_clear_text:
#     my_clear_text.write(text)
#
#
# Написать программу транслитерации с русского на английский и ноборот. Данные для транслитерации берутся в виде
# словарей из файла и записываются в другой файл. Направление перевода определяется через меню пользователя.
# ru_to_eng = {
#     'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
#     'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k',
#     'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
#     'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
#     'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
#     'э': 'e', 'ю': 'yu', 'я': 'ya',
# }
#
# eng_to_ru = {
#     'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'е',
#     'yo': 'ё', 'zh': 'ж', 'z': 'з', 'i': 'и', 'y': 'й', 'k': 'к',
#     'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'r': 'р',
#     's': 'с', 't': 'т', 'u': 'у', 'f': 'ф', 'kh': 'х', 'ts': 'ц',
#     'ch': 'ч', 'sh': 'ш', 'shch': 'щ', 'y': 'ы', 'e': 'э', 'yu': 'ю',
#     'ya': 'я',
# }
#
#
# def trans_text(text, direction):
#     if direction == "ru_to_eng":
#         translat = ru_to_eng
#     elif direction == "eng_to_ru":
#         translat = eng_to_ru
#     else:
#         print("Неверный ввод!")
#         return ""
#
#     result = ""
#     for char in text:
#         if char in translat:
#             result += translat[char]
#         else:
#             result += char
#     return result
#
#
# while True:
#     print('Меню:')
#     print("1. Перевод с русского на английский.")
#     print("2. Перевод с английского на русский.")
#     print('3. Выход.')
#     choice = int(input("Ваш выбор: "))
#     if choice == 1:
#         text = input("Введите текст на русском: ")
#         result = trans_text(text, "ru_to_eng")
#         with open(file='ru_to_eng_text.txt', mode='w', encoding='utf-8') as eng_text:
#             finally_text = eng_text.write(result)
#     elif choice == 2:
#         text = input("Введите ваш текст еа английском: ")
#         result = trans_text(text, "eng_to_ru")
#         with open(file='eng_to_ru_text.txt', mode='w', encoding='utf-8') as ru_text:
#             finally_text =ru_text.write(result)
#     elif choice == 3:
#         print('Выход из программы...')
#         break
#     else:
#         print("Неверный номер команды")



