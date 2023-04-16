# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора,
# цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы
# класса.

class Book:
    def __init__(self):
        self.book_dict = {'title': '',
                          'year': 0,
                          'publisher': '',
                          'genre': '',
                          'author': '',
                          'price': 0}

    def set_books(self, field_name, field_value):
        self.book_dict[field_name] = field_value

    def get_book(self, field_name):
        return self.book_dict[field_name]

    def input_book_data(self):
        self.set_books("title", input("Введите название книги: "))
        self.set_books("year", int(input("Введите год выпуска книги: ")))
        self.set_books("publisher", input("Введите издателя книги: "))
        self.set_books("genre", input("Введите жанр книги: "))
        self.set_books("author", input("Введите автора книги: "))
        self.set_books("price", float(input("Введите цену книги: ")))

    def print_book_data(self):
        print("Название книги: ", self.get_book("title"))
        print("Год выпуска книги: ", self.get_book("year"))
        print("Издатель книги: ", self.get_book("publisher"))
        print("Жанр книги: ", self.get_book("genre"))
        print("Автор книги: ", self.get_book("author"))
        print("Цена книги: ", self.get_book("price"))


my_book = Book()
my_book.input_car_data()
my_book.print_car_data()
