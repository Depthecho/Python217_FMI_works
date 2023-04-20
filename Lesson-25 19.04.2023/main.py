# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         if denominator != 0:
#             self.denominator = denominator
#         else:
#             raise ValueError('Invalid denominator')
#
#     def __add__(self, other):
#         new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
#         new_denominator = self.denominator * other.denominator
#         return Fraction(new_numerator, new_denominator)
#
#     def __sub__(self, other):
#         new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
#         new_denominator = self.denominator * other.denominator
#         return Fraction(new_numerator, new_denominator)
#
#     def __mul__(self, other):
#         new_numerator = self.numerator * other.numerator
#         new_denominator = self.denominator * other.denominator
#         return Fraction(new_numerator, new_denominator)
#
#     def __truediv__(self, other):
#         if other.self.numerator == 0:
#             return "0"
#         else:
#             new_numerator = self.numerator * other.denominator
#             new_denominator = self.denominator * other.numerator
#             return Fraction(new_numerator, new_denominator)
#
#     def __str__(self):
#         if self.numerator == 0:
#             return "0"
#         elif self.numerator == self.denominator:
#             return "1"
#         else:
#             return f"{self.numerator}/{self.denominator}"
#
#
# a = Fraction(4, 10)
# b = Fraction(2, 5)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
from xmlrpc.client import DateTime


# class Library:
#     def __init__(self, name, address, num_books, capacity):
#         self.name = name
#         self.address = address
#         self.num_books = num_books
#         self.capacity = capacity
#
#     def __add__(self, num_books):
#         return self.num_books + num_books
#
#     def __radd__(self, num_books):
#         return self.__add__(num_books)
#
#     def __iadd__(self, num_books):
#         self.num_books += num_books
#         return self
#
#     def __sub__(self, num_books):
#         return self.num_books - num_books
#
#     def __rsub__(self, num_books):
#         return self.__sub__(num_books)
#
#     def __isub__(self, num_books):
#         self.num_books -= num_books
#         return self
#
#     def __lt__(self, other):
#         return self.num_books < other.num_books
#
#     def __le__(self, other):
#         return self.num_books <= other.num_books
#
#     def __eq__(self, other):
#         return self.num_books == other.num_books
#
#     def __ne__(self, other):
#         return self.num_books != other.num_books
#
#     def __gt__(self, other):
#         return self.num_books > other.num_books
#
#     def __ge__(self, other):
#         return self.num_books >= other.num_books
#
#     def __str__(self):
#         return f"Библиотека {self.name} находится по адресу: {self.address}, вместимость людей: {self.capacity}," \
#                f" на даннный момен тимеется {self.num_books} книг."
#
#
# lib1 = Library("my_libr1", "my_adress1", 1000, 500)
# print(lib1)
# lib1 += 500
# print(lib1)
# lib1 -= 1000
# print(lib1)
# lib2 = Library("my_libr2", "my_adress2", 700, 500)
# print(lib1 > lib2)
# print(lib1 < lib2)
# print(lib1 >= lib2)
# print(lib1 <= lib2)
# print(lib1 == lib2)
# print(lib1 != lib2)
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def is_leap_year(self):
        return True if self.year % 400 == 0 or self.year % 100 == 0 or self.year % 4 == 0 else False

    def get_month_name(self):
        months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        return months[self.month]

    def get_days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month == 2:
            if self.is_leap_year():
                return 29
            else:
                return 28
        else:
            return 30

    def __sub__(self, other):
        days = 0
        if self > other:
            start_date = other
            end_date = self
        else:
            start_date = self
            end_date = other
        while start_date != end_date:
            days += 1
            start_date += 1
        return days

    def __add__(self, days):
        while days > 0:
            days_in_month = self.get_days_in_month()
            if self.day + days > days_in_month:
                days -= days_in_month - self.day + 1
                self.day = 1
                if self.month == 12:
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1
            else:
                self.day += days
                days = 0
        return self

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        else:
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            else:
                if self.day > other.day:
                    return True
                else:
                    return False

    def __lt__(self, other):
        return not self > other and self != other

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return not self > other

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return f"{self.day}:{self.month}:{self.year}"

first_date = Date(28, 8, 2002)
second_date = Date(28, 8, 2003)
print(first_date - second_date)
print(first_date)
first_date + 400
print(first_date)
