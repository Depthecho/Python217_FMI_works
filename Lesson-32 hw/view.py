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
              "1. Add new shoes\n"
              "2. Get shoes by filter\n"
              "3. Remove a shoes\n"
              "0. Exit the program\n")
        query = input("Enter ur command: ")
        return query

    @add_tittle('Adding shoes data')
    def get_file_data(self):
        properties = ['name', 'type of shoes(gender)', 'view', 'color', 'director', 'size']
        raw_data = [input(f"Input {property}: ") for property in properties]
        type_of_shoes = list(map(str.strip, raw_data[1].split(',')))
        data = raw_data[:1] + type_of_shoes + raw_data[2::1]
        return data

    @add_tittle('Find films by')
    def get_target(self):
        keywords = input("Enter keywords to find shoes, comma separated: ")
        return keywords

    @add_tittle('List of films')
    def print_shoes(self, shoes):
        [print(f'{i}, {shoe.to_str(i)}') for i, shoe in enumerate(shoes)]

    @add_tittle('Getting deletion context')
    def get_deletion_context(self, shoes):
        self.print_shoes(shoes)
        number = int(input('Enter number of shoes you want to delete: '))
        return number