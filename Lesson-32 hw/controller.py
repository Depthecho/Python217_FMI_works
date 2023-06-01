from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model('Shoes.csv')

    def run(self):
        query = None
        while query != '0':
            query = self.view.wait_user_answer()
            self.evaluate_user_answer(query)

    def evaluate_user_answer(self, query):
        if query == '1':
            shoes_data = self.view.get_file_data()
            self.model.add_new_shoes(shoes_data)
        elif query == '2':
            target = self.view.get_target()
            shoes = self.model.get_shoes_by(target)
            self.view.print_shoes(shoes)
        elif query == '3':
            target = self.view.get_target()
            shoes = self.model.get_shoes_by(target)
            if len(shoes) >1:
                number = self.view.get_deletion_context(shoes)
                shoes = [shoes[number-1]]
            self.model.delete_shoes(shoes[0])