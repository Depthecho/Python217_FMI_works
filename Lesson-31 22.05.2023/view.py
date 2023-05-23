def add_name(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(name.center(50, "="))
            result = func(*args, **kwargs)
            print("="*50)
            return result
        return wrapper
    return decorator


class View:
    @add_name('Waiting for user answer')
    def wait_user_answer(self):
        print("Available commands:\n"
              "1. add new article\n"
              "2. show all articles\n"
              "3. Search article\n"
              "4. Delete article\n"
              "'Exit'. Exit the application")
        query = input('Enter ur command: ')
        return query

    @add_name('Adding new article')
    def get_new_article_data(self):
        dict_article = {'Name': '',
                        'Author': '',
                        'Number of characters': '',
                        'Publication': '',
                        'Description': ''}
        for key in dict_article.keys():
            dict_article[key] = input(f"Enter {key.lower()} of article: ")
        return dict_article

    @add_name('List of articles')
    def show_articles(self, articles):
        if articles:
            [print(f'{i}. {art}') for i, art in enumerate(articles, 1)]
        else:
            print('There is not a single article')

    @add_name('Search articles by word')
    def get_keyword_to_find_articles(self):
        key_words = input('Enter list of words for search articles: ').split()
        return key_words

    @add_name("Article's name")
    def get_article_name_to_delete(self):
        article_name = input("Enter article's name: ")
        return article_name.strip()

    @add_name("Additional information")
    def get_deletion_context(self):
        number = input("Enter number for delete: ")
        return number

    @add_name("Result od remove")
    def return_delete_article(self, result):
        print(result)

    @add_name("Loading error")
    def throw_error(self, e):
        print("An error occurred while loading the database: ", e)
