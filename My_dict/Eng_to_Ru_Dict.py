DICTIONARY_FILE = 'dictionary.txt'


def load_dictionary():
    try:
        with open(DICTIONARY_FILE, 'r', encoding='utf-8') as f:
            dictionary = {}
            current_category = ''
            for line in f:
                line = line.strip()
                if line.startswith('[') and line.endswith(']'):
                    current_category = line[1:-1]
                    dictionary[current_category] = {}
                else:
                    english_word, russian_word, transcription = line.split(':')
                    dictionary[current_category][english_word] = {'russian': russian_word,
                                                                  'transcription': transcription}
            return dictionary
    except FileNotFoundError:
        return {}


def save_dictionary(dictionary):
    with open(DICTIONARY_FILE, 'w', encoding='utf-8') as f:
        for category, words in dictionary.items():
            f.write(f"[{category}]\n")
            for english_word, translation in words.items():
                russian_word = translation['russian']
                transcription = translation['transcription']
                f.write(f"{english_word} : {russian_word} : {transcription}\n")


def add_word(dictionary):
    category = input('Введите название категории: ')
    english_word = input('Введите английское слово: ')
    russian_word = input('Введите перевод на русский: ')
    transcription = input('Введите транскрипцию: ')
    if category not in dictionary:
        dictionary[category] = {}
    dictionary[category][english_word] = {'russian': russian_word, 'transcription': transcription}
    save_dictionary(dictionary)
    print('Слово добавлено в категорию и сохранено в файл')


def search_word(dictionary):
    search_word = input('Введите слово для поиска: ')
    for category, words in dictionary.items():
        if search_word in words:
            russian_word = words[search_word]['russian']
            transcription = words[search_word]['transcription']
            print(f"{category} : {search_word} : {russian_word} : {transcription}")
            return
    print('Слово не найдено в словаре')


def print_category(dictionary, category):
    if category not in dictionary:
        print(f"Категория '{category}' не найдена в словаре")
        return
    words = dictionary[category]
    for english_word, translation in words.items():
        russian_word = translation['russian']
        transcription = translation['transcription']
        print(f"{english_word} : {russian_word} : {transcription}")


def print_all_categories(dictionary):
    for category in dictionary.keys():
        print_category(dictionary, category)


def delete_category(dictionary):
    category_name = input('Введите название категории, которую нужно удалить: ')
    if category_name in dictionary:
        del dictionary[category_name]
        save_dictionary(dictionary)
        print(f'Категория "{category_name}" удалена')
    else:
        print(f'Категория "{category_name}" не найдена')


def delete_word_from_category(dictionary):
    category_name = input('Введите название категории, из которой нужно удалить слово: ')
    if category_name in dictionary:
        category = dictionary[category_name]
        english_word = input('Введите английское слово, которое нужно удалить: ')
        if english_word in category:
            del category[english_word]
            save_dictionary(dictionary)
            print(f'Слово "{english_word}" удалено из категории "{category_name}"')
        else:
            print(f'Слово "{english_word}" не найдено в категории "{category_name}"')
    else:
        print(f'Категория "{category_name}" не найдена')


def main():
    dictionary = load_dictionary()

    while True:
        print('Выберите действие:')
        print('1. Добавить слово в категорию')
        print('2. Найти слово в категории')
        print('3. Вывести все категории')
        print('4. Вывести все слова в категории')
        print('5. Удалить категорию')
        print('6. Удалить слово из категории')
        print('7. Выйти из программы')
        choice = input('Введите номер действия: \n')

        if choice == '1':
            add_word(dictionary)
        elif choice == '2':
            search_word(dictionary)
        elif choice == '3':
            print_all_categories(dictionary)
        elif choice == '4':
            category = input('Введите название категории: ')
            print_category(dictionary, category)
        elif choice == '5':
            delete_category(dictionary)
        elif choice == '6':
            delete_word_from_category(dictionary)
        elif choice == '7':
            break
        else:
            print('Введена неверная комаанда')


main()