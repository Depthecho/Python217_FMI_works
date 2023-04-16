# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город,
# вместимость. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через
# методы класса.

class Stadium:
    def __init__(self):
        self.stadium_dict = {'name': '',
                             'opening_date': '',
                             'country': '',
                             'city': '',
                             'capacity': 0}

    def set_stadiums(self, field_name, field_value):
        self.stadium_dict[field_name] = field_value

    def get_stadium(self, field_name):
        return self.stadium_dict[field_name]

    def input_stadium_data(self):
        self.set_stadiums("name", input("Введите название стадиона: "))
        self.set_stadiums("opening_date", input("Введите дату открытия стадиона: "))
        self.set_stadiums("country", input("Введите страну, в которой находится стадион: "))
        self.set_stadiums("city", input("Введите город, в котором находится стадион: "))
        self.set_stadiums("capacity", int(input("Введите вместимость стадиона: ")))

    def print_stadium_data(self):
        print("Название стадиона: ", self.get_stadium("name"))
        print("Дата открытия стадиона: ", self.get_stadium("opening_date"))
        print("Страна, в которой находится стадион: ", self.get_stadium("country"))
        print("Город, в котором находится стадион: ", self.get_stadium("city"))
        print("Вместимость стадиона: ", self.get_stadium("capacity"))


my_stadium = Stadium()
my_stadium.input_stadium_data()
my_stadium.print_stadium_data()
