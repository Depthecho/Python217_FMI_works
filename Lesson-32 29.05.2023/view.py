def add_tittle(tittle):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(tittle.center(50, '*'))
            result = func(*args, **kwargs)
            print('*' * 50)
            return result

        return wrapper

    return decorator


class View:
    @add_tittle('Awaiting for user input')
    def wait_user_answer(self):
        print("List of commands:\n"
              "1. Add new film\n"
              "2. Get files by filter\n"
              "3. Remove a film\n"
              "0. Exit the program\n")
        query = input("Enter ur command: ")
        return query

    @add_tittle('Adding film data')
    def get_file_data(self):
        properties = ['title', 'genres(comma separated', 'director', 'year', 'length', 'studio', 'actors(Actor:Role,..']
        raw_data = [input(f"Input {property}: ") for property in properties]
        genres = list(map(str.strip, raw_data[1].split(',')))
        actors = [row.strip().split(':') for row in raw_data[-1].split(',')]
        data = raw_data[:1] + genres + raw_data[2:-1]
        [data.extend(row) for row in actors]
        return data

    @add_tittle('Find films by')
    def get_target(self):
        keywords = input("Enter keywords to find films, comma separated: ")
        return keywords

    @add_tittle('List of films')
    def print_films(self, films):
        [print(f'{i}, {film.to_str(i)}') for i, film in enumerate(films)]

    @add_tittle('Getting deletion context')
    def get_deletion_context(self, films):
        self.print_films(films)
        number = int(input('Enter numberr of film you want to delete: '))
        return number