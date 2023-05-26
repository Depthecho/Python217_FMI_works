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
            recept_data = self.view.get_new_recept_data()
            self.model.add_new_recept(recept_data)
        if query == "2":
            recepts = self.model.recepts
            self.view.show_recept(recepts)
        elif query == "3":
            key_words = self.view.get_keyword_to_find_articles()
            recepts = self.model.find_recepts(key_words)
            self.view.show_recept(recepts)
        elif query == "4":
            recept_name = self.view.get_recept_name_to_delete()
            recepts = self.model.find_recepts(recept_name)
            result = self.model.delete_recept(recepts)
            if result == 'So many articles':
                self.view.show_recept(recepts)
                number = self.view.get_deletion_context()
                result = self.model.delete_recept(recepts[number-1])
            self.view.return_delete_recept(result)