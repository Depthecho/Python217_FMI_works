# К уже реализованному классу «Стадион» добавьте возможность упаковки и распаковки данных с использованием json и
# pickle.

import json
import pickle


class Stadium:
    def __init__(self, name, year, capacity):
        self.name = name
        self.year = year
        self.capacity = capacity

    def stadium_description(self):
        print(f"Стадион '{self.name}' был построен в {self.year} году и имеет вместимость {self.capacity} человек(а).")

    def pack_pickle(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def unpack_pickle(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)

    def pack_json(self, filename):
        with open(filename, "w") as file:
            json.dump({"name": self.name, "year": self.year, "capacity": self.capacity}, file)

    @staticmethod
    def unpack_json(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return Stadium(data["name"], data["year"], data["capacity"])


my_stadium = Stadium("My stadium", 2019, 50000)
my_stadium.pack_pickle("stadium.txt")
my_stadium = Stadium.unpack_pickle("stadium.txt")
my_stadium.stadium_description()