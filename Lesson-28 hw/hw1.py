# К уже реализованному классу «Автомобиль» добавьте возможность упаковки и распаковки данных с использованием json и
# pickle.

import json
import pickle


class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self.year = year
        self.mileage = mileage

    def car_mileage(self):
        print(f"На данный момент времени пробег машины {self.model} составляет {self.mileage} км.")

    def pack_pickle(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def unpack_pickle(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)

    def pack_json(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump({"model": self.model, "year": self.year, "mileage": self.mileage}, file)

    @staticmethod
    def unpack_json(filename):
        with open(filename, "r", encoding="utf-8") as file:
            car_options = json.load(file)
        return Car(car_options["model"], car_options["year"], car_options["mileage"])


my_car = Car("BMW X5", 2021, 75000)
my_car.pack_pickle("my_car.txt")
my_car = Car.unpack_pickle("my_car.txt")
my_car.car_mileage()

my_car2 = Car("Mercedes-Benz", 2018, 15000)
my_car2.pack_json("my_car2.txt")
my_car2 = Car.unpack_json("my_car2.txt")
my_car2.car_mileage()