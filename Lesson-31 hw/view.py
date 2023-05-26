def add_name(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(name.center(50, "="))
            result = func(*args, **kwargs)
            print("=" * 50)
            return result

        return wrapper

    return decorator


class View:
    @add_name('Waiting for user answer')
    def wait_user_answer(self):
        print("Available commands:\n"
              "1. add new recept\n"
              "2. show all recepts\n"
              "3. Search recept\n"
              "4. Delete recept\n"
              "'Exit'. Exit the application")
        query = input('Enter ur command: ')
        return query

    @add_name('Adding new article')
    def get_new_recept_data(self):
        dict_recept = {'Name of recept': '',
                       'Author of recept': '',
                       'Type of recept': '',
                       'Description of recept': '',
                       'list of ingredients': '',
                       'Name_of_kitchen': ''}
        for key in dict_recept.keys():
            dict_recept[key] = input(f"Enter {key.lower()} of recept: ")
        return dict_recept

    @add_name('List of recepts')
    def show_recept(self, recepts):
        if recepts:
            [print(f'{i}. {rec}') for i, rec in enumerate(recepts, 1)]
        else:
            print('There is not a single recept')

    @add_name('Search recepts by word')
    def get_keyword_to_find_articles(self):
        key_words = input('Enter list of words for search articles: ').split()
        return key_words

    @add_name("Rcept's name")
    def get_recept_name_to_delete(self):
        article_name = input("Enter article's name: ")
        return article_name.strip()

    @add_name("Additional information")
    def get_deletion_context(self):
        number = input("Enter number for delete: ")
        return number

    @add_name("Result od remove")
    def return_delete_recept(self, result):
        print(result)

    @add_name("Loading error")
    def throw_error(self, e):
        print("An error occurred while loading the database: ", e)
