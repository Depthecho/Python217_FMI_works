# Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах: автор, название книги, жанр, год выпуска,
# количество страниц, издательство. Требуется реализовать возможность добавления, удале-ния, поиска, замены данных.
# Используйте словарь для хранения информации.

books_collection = {input('Enter ur author\'s name and book title: '): {
    'genre': input('Enter genre of the book: '),
    'year of release': input('Enter year of release: '),
    'number of pages': input('Enter number of pages: '),
    'publisher': input('Enter publisher of the book: ')}}
print(books_collection)

while True:
    command = input('Enter ur command (add / delete / search / substitute / end ): ')
    if command == 'add':
        word = input('Enter the author and the title of the book whose data you want to add: ')
        word2, word3 = input('What do u want to add?: '), input('Enter new data:')
        books_collection[word][word2] = word3
        print(books_collection)
    elif command == 'delete':
        word = input('Which collection do u want to delete?: ')
        books_collection.pop(word)
        print(books_collection)
    elif command == 'search':
        word = input('Which collection do u want to search?: ')
        if word in books_collection:
            print(f'Yes, there is this book in this collection: {books_collection[word]}')
        else:
            print(f'No, there is no such book in this collection: {word}')
    if command == 'substitute':
        word = input('Enter the author and the title of the book whose data u want to change: ')
        word2, word3 = input('What do u want to change?: '), input('Enter new data:')
        books_collection[word][word2] = word3
        print(books_collection)
    elif command == 'end':
        break
    else:
        print('Invalid command')

