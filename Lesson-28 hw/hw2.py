# К уже реализованному классу «Книга» добавьте возможность упаковки и распаковки данных с использованием json и
# pickle.

import json
import pickle


class Book:
    def __init__(self, author, title, year, pages):
        self.author = author
        self.title = title
        self.year = year
        self.pages = pages

    def book_description(self):
        print(f"Книга {self.title} от {self.author} выпущена в {self.year} году и состоит из {self.pages} страниц(ы)")

    def pack_pickle(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @staticmethod
    def unpack_pickle(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)

    def pack_json(self, filename):
        with open(filename, "w") as file:
            json.dump({"author": self.author, "title": self.title, "year": self.year, "pages": self.pages}, file)

    @staticmethod
    def unpack_json(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return Book(data["author"], data["title"], data["year"], data["pages"])


my_book = Book("I. S. Turgenev", "Fathers and Sons", 1862, 537)
my_book.pack_pickle("book1.txt")
unpacked_book1 = Book.unpack_pickle("book1.txt")
my_book.book_description()

my_book2 = Book("F. M. Dostoevskiy", "Crime and Punishment", 1866, 427)
my_book2.pack_json("book2.txt")
unpacked_book2 = Book.unpack_json("book2.txt")
my_book2.book_description()
