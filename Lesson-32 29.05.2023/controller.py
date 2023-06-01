from model import Model
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model('Films.csv')

    def run(self):
        query = None
        while query != '0':
            query = self.view.wait_user_answer()
            self.evaluate_user_answer(query)

    def evaluate_user_answer(self, query):
        if query == '1':
            film_data = self.view.get_file_data()
            self.model.add_new_film(film_data)
        elif query == '2':
            target = self.view.get_target()
            films = self.model.get_films_by(target)
            self.view.print_films(films)
        elif query == '3':
            target = self.view.get_target()
            films = self.model.get_films_by(target)
            if len(films) >1:
                number = self.view.get_deletion_context(films)
                films = [films[number-1]]
            self.model.delete_film(films[0])

