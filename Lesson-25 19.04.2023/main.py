# class Car:
#     def __init__(self, naming, year, producer,
#                  volume_of_engine, color, price):
#         self.naming = naming
#         self.year = year
#         self.producer = producer
#         self.volume_of_engine = volume_of_engine
#         self.color = color
#         self.price = price
#
#     def print_info(self):
#         print(f'Автомобиль: {self.naming}\n'
#               f'Год выпуска: {self.year}\n'
#               f'Производитель: {self.producer}\n'
#               f'Объём двигателя: {self.volume_of_engine}\n'
#               f'Цвет машины: {self.color}\n'
#               f'Цена: {self.price}')
#
#     def reset_info(self):
#         self.naming = input(f'Автомобиль: ')
#         self.year = input(f'Год выпуска: ')
#         self.producer = input(f'Производитель: ')
#         self.volume_of_engine = input(f'Объём двигателя: ')
#         self.color = input(f'Цвет машины: ')
#         self.price = input(f'Цена: ')
#
#
# car = Car(1, 2, 3, 4, 5, 6)
# car.print_info()
# car.reset_info()
# car.print_info()


# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         if other.value < 5:
#             print('Я не хочу складывать себя с этим ужасным объектом')
#             return self.value
#         return self.value + other.value
#
#     def __sub__(self, other):
#         pass
#
#     def __mul__(self, other):
#         pass
#
#     def __truediv__(self, other):
#         pass
#
#     def __pow__(self, power, modulo=None):
#         pass
#
#     def __floordiv__(self, other):
#         pass
#
#     def __mod__(self, other):
#         pass
#
#
# a = MyClass(4)
# b = MyClass(1)
# print(a + b)
# print(a - b)
# print(b / a)
# print(a ** 2)
# print(a // 2)
# print(a % 2)


# 1.

# class MyInt:
#     def __init__(self, value):
#         if isinstance(value, int | float):
#             self.value = int(value)
#         else:
#             raise ValueError('Из этого нельзя сделать число!')
#
#     def __add__(self, other):
#         return self.value + other.value
#
#     def __sub__(self, other):
#         return self.value - other.value
#
#     def __mul__(self, other):
#         return self.value * other.value
#
#     def __truediv__(self, other):
#         if other.value == 0:
#             raise ZeroDivisionError('Нельзя делить на ноль!')
#         return self.value / other.value
#
#
# a = MyInt(5)
# b = MyInt(12)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)


## Логические операторы и другие операторы
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return self.value + other.value
#
#     def __radd__(self, other):
#         return self.__add__(other)
#
#     def __eq__(self, other):
#         return self.value == other.value
#
#     def __ne__(self, other):
#         return self.value != other.value
#
#     def __lt__(self, other):
#         return self.value < other.value
#
#     def __le__(self, other):
#         return self.value <= other.value
#
#     def __gt__(self, other):
#         return self.value > other.value
#
#     def __ge__(self, other):
#         return self.value >= other.value
#
#     def __str__(self):
#         return f'{self.__class__.__name__} Object = {self.value}'
#
#
# from random import randint
#
# lst = [MyClass(randint(1, 5)) for i in range(10)]
# lst.sort()
# for obj in lst:
#     print(obj)
#
#
# a = MyClass(5)
# b = MyClass(3)
# a += b
# print(a)


# 2.

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
#         def __truediv__(self, other):
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


# 3.

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


# 4.

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def __str__(self):
#         return f"{self.day}/{self.month}/{self.year}"
#
#     def is_leap_year(self=None, year=None):
#         if self:
#             return (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0
#         return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
#
#     @staticmethod
#     def days_in_month(month, year):
#         if Date.is_leap_year(year=year):
#             return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
#         return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
#
#     def __sub__(self, other):
#         days = 0
#
#         start, end = min(self.year, other.year), max(self.year, other.year)
#         for year in range(start, end):
#             if self.is_leap_year():
#                 days += 366
#             else:
#                 days += 365
#
#         start, end = min(self.month, other.month), max(self.month, other.month)
#         for month in range(start, end):
#             days += Date.days_in_month(month, self.year)
#
#         days += abs(self.day - other.day)
#         return days
#
#     def __iadd__(self, days):
#         day = self.day + days
#         month = self.month
#         year = self.year
#         while day > Date.days_in_month(month, year):
#             day -= Date.days_in_month(month, year)
#             month += 1
#             if month > 12:
#                 month = 1
#                 year += 1
#         return Date(day, month, year)
#
#
# a = Date(1, 1, 2000)
# b = Date(30, 4, 2000)
# print(a - b)
# a += 366
# print(a)
# a += 189
# print(a)
