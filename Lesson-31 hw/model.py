import json


class Recept:
    def __init__(self, name_of_recept, author_of_recept, tyoe_of_recept, description_of_recept, list_of_ingredients,
                 name_of_kitchen):
        self.name_of_recept = name_of_recept
        self.author_of_recept = author_of_recept
        self.tyoe_of_recept = tyoe_of_recept
        self.description_of_recept = description_of_recept
        self.list_of_ingredients = list_of_ingredients
        self.name_of_kitchen = name_of_kitchen

    def __str__(self):
        return f"Recept '{self.name_of_recept}' by {self.author_of_recept}:" \
               f" Type: {self.tyoe_of_recept}" \
               f" Description: {self.description_of_recept} " \
               f" Ingredients: {self.list_of_ingredients}" \
               f" Name of kitchen:  {self.name_of_kitchen}"


class DecodeError(Exception):
    pass


class Model:
    def __init__(self, filepath):
        self.filepath = filepath
        self.__recepts = {}
        try:
            self.data = json.load(open(self.filepath, "r", encoding="utf-8"))
            for recept in self.data.values():
                self.__recepts[f'{recept["name_of_recept"]} {recept["author_of_recept"]}'] = Recept(*recept.values())
        except json.JSONDecodeError:
            raise DecodeError
        except FileNotFoundError:
            with open(self.filepath, "w") as f:
                f.write('{}')

    @property
    def recepts(self):
        return self.__recepts

    def save_recepts(self):
        dict_recepts = {f'{rec.name_of_recept} {rec.author_of_recept}': rec.__dict__ for rec in self.__recepts.values()}
        json.dump(dict_recepts, open(self.filepath, "w", encoding="utf-8"))

    def add_new_recept(self, recept_data):
        new_recept = Recept(*recept_data.values())
        self.__recepts[f'{new_recept.name_of_recept} {new_recept.author_of_recept}'] = new_recept
        self.save_recepts()

    def find_recepts(self, key_words):
        recepts = []
        for recept in self.__recepts.values():
            for word in key_words:
                if recept in recepts:
                    break
                for prop in recept.__dict__.values():
                    if word.lower() in prop.lower():
                        recepts.append(recept)
                        break
        return recepts

    def delete_recept(self, recepts):
        if len(recepts) == 0:
            return "No such recept was found"
        elif len(recepts) == 1:
            recept = recepts[0]
            key = f'{recept.name_of_recept} {recept.author_of_recept}'
            self.__recepts.pop(key)
            self.save_recepts()
            return "Recept has been deleted"
        elif len(recepts) > 1:
            return "So many recepts"
