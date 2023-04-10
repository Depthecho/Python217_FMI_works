# Создайте программу «Англо-французский словарь». Нужно хранить слово на английском языке и его перевод на французский.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь
# для хранения информации.
eng_to_french_dic = {'cat': 'chat', 'dog': 'chien'}

while True:
    command = input('Enter ur command (add / delete / search / substitute / end ): ')
    if command == 'add':
        word = input('Enter eng word to add: ')
        word2 = input('Enter french word for ur eng word: ')
        eng_to_french_dic[word] = word2
        print(eng_to_french_dic)
    elif command == 'delete':
        word = input('Enter eng word to delete: ')
        eng_to_french_dic.pop(word)
        print(eng_to_french_dic)
    elif command == 'search':
        word = input('Enter eng word to search: ')
        if word in eng_to_french_dic:
            print(f'Yes, there is such a word in the dictionary, it is:{eng_to_french_dic[word]}')
    elif command == 'substitute':
        word = input('Enter eng word to substitute: ')
        word2 = input('Enter french word for ur eng word: ')
        eng_to_french_dic[word] = word2
        print(eng_to_french_dic)
    elif command == 'end':
        print('The program is completed')
        break
    else:
        print('Invalid command')
