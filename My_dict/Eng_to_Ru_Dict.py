DICTIONARY_FILE = 'dictionary.txt'


def load_dictionary():
    try:
        with open('dictionary.txt', 'r', encoding='utf-8') as f:
            dictionary = {}
            for line in f:
                english_word, russian_word, transcription = line.strip().split('|')
                dictionary[english_word] = {'russian': russian_word, 'transcription': transcription}
            return dictionary
    except FileNotFoundError:
        return {}


def save_dictionary(dictionary):
    with open('dictionary.txt', 'w', encoding='utf-8') as f:
        for english_word, translation in dictionary.items():
            russian_word = translation['russian']
            transcription = translation['transcription']
            f.write(f"{english_word} : {russian_word} : {transcription}\n")


def add_word(dictionary):
    english_word = input('Введите английское слово: ')
    russian_word = input('Введите перевод на русский: ')
    transcription = input('Введите транскрипцию: ')
    dictionary[english_word] = {'russian': russian_word, 'transcription': transcription}
    save_dictionary(dictionary)
    print('Слово добавлено в словарь и сохранено в файл')


def search_word(dictionary):
    search_word = input('Введите слово для поиска: ')
    if search_word in dictionary:
        russian_word = dictionary[search_word]['russian']
        transcription = dictionary[search_word]['transcription']
        print(f"{search_word}: {russian_word}: {transcription}")
    else:
        print('Слово не найдено в словаре')


def print_dictionary(dictionary):
    for english_word, translation in dictionary.items():
        russian_word = translation['russian']
        transcription = translation['transcription']
        print(f"{english_word}: {russian_word}: {transcription}")


def main():
    dictionary = load_dictionary()

    while True:
        print('Выберите действие:')
        print('1. Добавить слово в словарь')
        print('2. Найти слово в словаре')
        print('3. Вывести все слова в словаре')
        print('4. Выйти из программы')
        choice = input('Введите номер действия: \n')

        if choice == '1':
            add_word(dictionary)
        elif choice == '2':
            search_word(dictionary)
        elif choice == '3':
            print_dictionary(dictionary)
        elif choice == '4':
            break
        else:
            print('Неверный выбор')


if __name__ == '__main__':
    main()