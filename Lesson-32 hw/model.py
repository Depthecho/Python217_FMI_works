from csv import reader, writer
import sys


class Shoes:
    type_of_shoes = ['Male', 'Female']

    def __init__(self, name, type_of_shoes, view, color, director, size):
        self.name = name
        self.type_of_shoes = type_of_shoes
        self.view = view
        self.color = color
        self.director = director
        self.size = size

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
                    self.database.append(self.__string_to_shoes__(string))
        except FileNotFoundError:
            print("Error in logging database! Proceed with empty data.", file=sys.stderr)

    @staticmethod
    def __string_to_shoes__(string):
        name = string.pop(0)
        type_of_shoes = []
        while string[0] in Shoes.type_of_shoes:
            type_of_shoes.append(string.pop(0))
        view = string.pop(0)
        color = string.pop(0)
        director = string.pop(0)
        size = string.pop(0)
        return Shoes(name, type_of_shoes, view, color, director, size)

    @staticmethod
    def __shoes_to_string__(shoes):
        result = [shoes.name]
        result.extend([shoes.type_of_shoes, shoes.view, shoes.color, shoes.director, shoes.size])
        return result

    def __save_data__(self):
        with open(self.filename, 'w', encoding='utf-8', newline='') as csv_file:
            data_writer = writer(csv_file)
            data_writer.writerows(map(self.__shoes_to_string__, self.database))

    def add_new_shoes(self, shoes_data):
        if self.database[1] in ['Female', 'Male']:
            self.database.append(self.__string_to_shoes__(shoes_data))
            self.__save_data__()
        else:
            print("Wrong type of shoes, We can't create these shoes")

    def get_shoes_by(self, keywords):
        keywords = list(map(str.strip, keywords.split(',')))
        shoes = []
        for keyword in keywords:
            for shoe in self.database:
                if keyword in ''.join(map(str, shoe.__dict__.values())) and shoe not in shoes:
                    shoes.append(shoe)
        return shoes

    def delete_shoes(self, shoe):
        self.database.remove(shoe)
        self.__save_data__()

