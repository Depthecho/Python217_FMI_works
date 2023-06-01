from csv import reader, writer
import sys


class Film:
    genres = ['Crime', 'Drama', 'Action', 'Biography', 'History', 'Adventure', 'Romance', 'Sci-Fi', 'Thriller', 'War',
              'Fantasy', 'Animation']

    def __init__(self, tittle, genre, directors, year, length, studio, actors):
        self.tittle = tittle
        self.genre = genre
        self.directors = directors
        self.year = year
        self.length = length
        self.studio = studio
        self.actors = actors

    def to_str(self, number):
        result = ''
        values = []
        for value in self.__dict__.values():
            if isinstance(value, list):
                value = ', '.join(map(str, value))
            if isinstance(value, dict):
                value = ', '.join(map(lambda pair: f'{str(pair[0])}, {str(pair[1])}', value.items()))
            values.append(value)

        maxes = [max([len(key), len(value), 7]) for key, value in self.__dict__.items()]

        for i, key in enumerate(self.__dict__.keys()):
            result += key.ljust(maxes[i], ' ')
            result += '| '
        result += '\n' + ' ' * len(str(number)) + '  '

        for i, key in enumerate(self.__dict__.keys()):
            result += values[i].ljust(maxes[i], ' ')
            result += '| '
        result += '\n'

        return result


class Model:
    def __init__(self, filename):
        self.filename = filename
        self.database = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = reader(f)
                for string in data:
                    self.database.append(self.__string_to_film__(string))
        except FileNotFoundError:
            print("Error in logging database! Proceed with empty data.", file=sys.stderr)

    @staticmethod
    def __string_to_film__(string):
        tittle = string.pop(0)
        genres = []
        while string[0] in Film.genres:
            genres.append(string.pop(0))
        directors = []
        while not string[0].isdigit():
            directors.append(string.pop(0))
        year = string.pop(0)
        length = string.pop(0)
        studio = string.pop(0)
        actors = {string[i]: string[i+1] for i in range(0, len(string) - 1, 2)}
        return Film(tittle, genres, directors, year, length, studio, actors)

    @staticmethod
    def __film_to_string__(film):
        result = [film.tittle]
        result.extend(film.genres)
        result.extend(film.directors)
        result.extend([film.year, film.length, film.studio])
        [(result.append(key), result.append(value)) for key, value in film.actors.items()]

    def __save_data__(self):
        with open(self.filename, 'w', encoding='utf-8', newline='') as csv_file:
            data_writer = writer(csv_file)
            data_writer.writerows(map(self.__film_to_string__, self.database))

    def add_new_film(self, film_data):
        self.database.append(self.__string_to_film__(film_data))
        self.__save_data__()

    def get_films_by(self, keywords):
        keywords = list(map(str.strip, keywords.split(',')))
        films = []
        for keyword in keywords:
            for film in self.database:
                if keyword in ''.join(map(str, film.__dict__.values())) and film not in films:
                    films.append(film)
        return films

    def delete_film(self, film):
        self.database.remove(film)
        self.__save_data__()

