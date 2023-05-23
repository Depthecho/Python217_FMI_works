from model import Model, DecodeError
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        try:
            self.model = Model('db.txt')
        except DecodeError as e:
            self.view.throw_an_error(e)

    def run(self):
        query = None
        while query != "Exit":
            query = self.view.wait_user_answer()
            self.resolve_user_answer(query)

    def resolve_user_answer(self, query):
        if query == "1":
            article_data = self.view.get_new_article_data()
            self.model.add_new_article(article_data)
        if query == "2":
            articles = self.model.articles
            self.view.show_articles(articles)
        elif query == "3":
            key_words = self.view.get_keyword_to_find_articles()
            articles = self.model.find_articles(key_words)
            self.view.show_articles(articles)
        elif query == "4":
            article_name = self.view.get_article_name_to_delete()
            articles = self.model.find_articles(article_name)
            result = self.model.delete_article(articles)
            if result == 'So many articles':
                self.view.show_articles(articles)
                number = self.view.get_deletion_context()
                result = self.model.delete_article(articles[number-1])
            self.view.return_delete_article(result)


