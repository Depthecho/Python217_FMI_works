# class Person():
#     def __init__(self):
#         self.person = dict()
#
#     def add_person(self):
#         self.person['first_name'] = input('Введите ваше имя: ')
#         self.person['second_name'] = input('Введите вашу фамилию: ')
#         self.person['third_name'] = input('Введите ваше отчество: ')
#         self.person['bday'] = input('Введите вашу дату рождения: ')
#         self.person['number_phone'] = input('Введите ваш номер телефона: ')
#         self.person['city'] = input('Введите ваш город: ')
#         self.person['country'] = input('Введите вашу страну: ')
#         self.person['adress'] = input('Введите ваш адрес: ')
#         print(self.person)
#
#     def show_person(self):
#         second_name = input('Введиет фмилию для поиска: ')
#         if second_name == self.person['second_name']:
#             self.person.pop('second_name')
#             for i in self.person.values():
#                 print(f"{i}", end=' ')
#
#
# my_person = Person()
# my_person.add_person()
# my_person.show_person()
#
#
# class Fraction():
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#
#     def input_fraction(self):
#         self.numerator = int(input("Введите числитель: "))
#         self.denominator = int(input("Введите знаменатель: "))
#
#     def summ_fraction(self, other):
#         summ_num = self.numerator * other.denominator + other.numerator * self.denominator
#         summ_den = self.denominator * other.denominator
#         print(f'{summ_num}/{summ_den}')
#         return Fraction(summ_num, summ_den)
#
#     def sub_fraction(self, other):
#         sub_num = self.numerator * other.denominator - other.numerator * self.denominator
#         sub_den = self.denominator * other.denominator
#         print(f'{sub_num}/{sub_den}')
#         return Fraction(sub_num, sub_den)
#
#     def multi_fraction(self, other):
#         multi_num = self.numerator * other.numerator
#         multi_den = self.denominator * other.denominator
#         print(f'{multi_num}/{multi_den}')
#         return Fraction(multi_num, multi_den)
#
#     def div_fraction(self, other):
#         div_num = self.numerator * other.denominator
#         div_den = self.denominator * other.numerator
#         print(f'{div_num}/{div_den}')
#         return Fraction(div_num, div_den)
#
#
# my_first_fraction = Fraction(4, 5)
# my_second_fraction = Fraction(6, 9)
# my_summ =my_first_fraction.summ_fraction(my_second_fraction)
# my_sub = my_first_fraction.sub_fraction(my_second_fraction)
# my_multi = my_first_fraction.multi_fraction(my_second_fraction)
# my_div = my_first_fraction.div_fraction(my_second_fraction)

# 25 cw
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