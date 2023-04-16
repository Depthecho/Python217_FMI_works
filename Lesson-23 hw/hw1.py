# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска, произво-дителя,
# объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных, реа-лизуйте доступ к
# отдельным полям через методы класса.


class Auto():
    def __init__(self):
        self.car_dict = {
            "model": "",
            "year": 0,
            "manufacturer": "",
            "engine_volume": 0,
            "color": "",
            "price": 0
        }

    def set_cars(self, dict_key, dict_value):
        self.car_dict[dict_key] = dict_value

    def get_car(self, field_name):
        return self.car_dict[field_name]

    def input_car_data(self):
        self.set_cars("model", input("Введите модель автомобиля: "))
        self.set_cars("year", int(input("Введите год выпуска автомобиля: ")))
        self.set_cars("manufacturer", input("Введите производителя автомобиля: "))
        self.set_cars("engine_volume", int(input("Введите объем двигателя автомобиля: ")))
        self.set_cars("color", input("Введите цвет автомобиля: "))
        self.set_cars("price", int(input("Введите цену автомобиля: ")))

    def print_car_data(self):
        print("Модель автомобиля:", self.get_car("model"))
        print("Год выпуска автомобиля:", self.get_car("year"))
        print("Производитель автомобиля:", self.get_car("manufacturer"))
        print("Объем двигателя автомобиля:", self.get_car("engine_volume"))
        print("Цвет автомобиля:", self.get_car("color"))
        print("Цена автомобиля:", self.get_car("price"))


my_auto = Auto()
my_auto.input_car_data()
my_auto.print_car_data()
