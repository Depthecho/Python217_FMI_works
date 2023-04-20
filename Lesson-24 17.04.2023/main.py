# class Number:
#     def __init__(self, num):
#         self.num = num
#
#     def add(self, other):
#         return Number(self.num + other.num)
#
#     @staticmethod
#     def get():
#         return 0
#
#     @classmethod
#     def print_info(cls):
#         print(cls.__name__)
#
#
# class Float(Number):
#     pass
#
#
# a = Number(2)
# print(a.get())
# Number.print_info()
# b = Float(3.4)
# b.print_info()


# class Human:
#     count = 0
#
#     def __init__(self, fio, dob, phone_number,
#                  city, country, adress):
#         self.fio = fio
#         self.dob = dob
#         self.phone_number = phone_number
#         self.city = city
#         self.country = country
#         self.adress = adress
#         self.__class__.count += 1
#
#     def reset(self):
#         self.fio = input('Введите новое ФИО: ')
#         self.dob = input('Введите новую дату рождения: ')
#         self.phone_number = input('Введите новый телефонный номер: ')
#         self.city = input('Введите новый город: ')
#         self.country = input('Введите новую страну: ')
#         self.adress = input('Введите новый адрес: ')
#
#     def print_info(self):
#         print(f'Фио: {self.fio}')
#         print(f'Дата рождения: {self.dob}')
#         print(f'Телефонный номер: {self.phone_number}')
#         print(f'Город: {self.city}')
#         print(f'Страна: {self.country}')
#         print(f'Адрес: {self.adress}')
#
#     @staticmethod
#     def get_count():
#         return Human.count
#
#
# print(Human.get_count())
# a = Human(5, 2, 3, 4, 4, 4)
# print(a.get_count())
# b = Human(5, 2, 3, 4, 4, 4)
# print(Human.get_count())


# class GeometrySquares:
#     count = 0
#
#     @staticmethod
#     def get_count():
#         return GeometrySquares.count
#
#     @staticmethod
#     def triangle_area_height(a, h):
#         GeometrySquares.count += 1
#         return a * h / 2
#
#     @staticmethod
#     def triangle_area_p(a, b, c):
#         GeometrySquares.count += 1
#         p = (a + b + c) / 2
#         return (p*(p - a)*(p - b)*(p - c))**0.5
#
#     @staticmethod
#     def rectangle_area(a, b):
#         GeometrySquares.count += 1
#         return a * b
#
#     @staticmethod
#     def square_area(a):
#         GeometrySquares.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rhombus_area(a, h):
#         GeometrySquares.count += 1
#         return a * h
#
#
# a = GeometrySquares.triangle_area_height(2, 6)
# print(a)
# a = GeometrySquares.triangle_area_p(2, 5, 4)
# print(a)
# print(GeometrySquares.get_count())


# class Circle:
#     def __init__(self, rad):
#         self.r = rad
#         self.__area = rad ** 2 * 3.14
#
#     @property
#     def area(self):
#         return self.__area
#
#     @area.setter
#     def area(self, value):
#         self.r = (value / 3.14) ** 0.5
#         self.__area = self.r ** 2 * 3.14
#
#     @area.deleter
#     def area(self):
#         raise Exception('НЕ ПЫТАЙТЕСЬ УДАЛИТЬ ЭТО СВОЙСТВО. ОНО СВЯЩЕННО')
#
#
# c = Circle(5)
# print(c.r, c.area)
# c.area = 5
# print(c.r, c.area)
# del c.area
# print(c.area)


# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     def __init__(self, name, age, sound):
#         self.name = name
#         self.age = age
#         self.sound = sound
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Cat(Animal):
#     def make_sound(self):
#         print(self.sound)
#
#
# cat = Cat('Мурзик', 2, 'Meow')
# cat.make_sound()


# from abc import ABC, abstractmethod
#
#
# class Human(ABC):
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def get_info(self):
#         pronoun = 'he' if self.sex == 'm' else 'she'
#         return f'This is {self.name}. {pronoun.capitalize()} is {self.age}. ' \
#                f'And {pronoun} is {self.occupation}'
#
#     @abstractmethod
#     def occupation(self):
#         pass
#
#     @abstractmethod
#     def say_something(self):
#         pass
#
#
# class Builder(Human):
#     @property
#     def occupation(self):
#         return 'Builder'
#
#     def say_something(self):
#         print('What do you want me to say?')
#
#
# class Sailor(Human):
#     @property
#     def occupation(self):
#         return 'Sailor'
#
#     def say_something(self):
#         print('Weather is kinda stormy today. Not good.')
#
#
# class Pilot(Human):
#     @property
#     def occupation(self):
#         return 'Pilot'
#
#     def say_something(self):
#         print('Get back in place and fasten your seatbelt!')
#
#
# c = Builder('Emma', 29, 'w')
# print(c.get_info())
# c.say_something()
# print('--------------')
#
# a = Sailor('John', 23, 'm')
# print(a.get_info())
# a.say_something()
# print('--------------')
#
# b = Pilot('Jeremy', 37, 'm')
# print(b.get_info())
# b.say_something()
