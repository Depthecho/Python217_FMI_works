# 1. Дз на 10.04.23
# with open('file1.txt', 'r') as file_1, open('file2.txt', 'r') as file_2:
#     text_1, text_2 = file_1.readlines(), file_2.readlines()
#     for line1, line2 in zip(text_1, text_2):
#         line1 = line1[:-1]
#         line2 = line2[:-1]
#         if line1 != line2:
#             print(f'Строки неравны: {line1}, {line2}')

# 2.
# with open('file1.txt', 'r') as file_1, open('file2.txt', 'w') as file_2:
#     text = file_1.read()
#     count_symboles = len(text)
#     count_strings = text.count('\n') + 1
#     vowels = 'euioa'
#     consonants = 'qwrtypsdfghjklzxcvbnm'
#     digits = '1234567890'
#     count_vowels = count_consonants = count_digits = 0
#     for symbol in text:
#         if symbol in vowels:
#             count_vowels += 1
#         elif symbol in consonants:
#             count_consonants += 1
#         elif symbol in digits:
#             count_digits += 1
#     file_2.write(' '.join(map(str, [count_strings, count_symboles,
#                                     count_vowels, count_consonants,
#                                     count_digits])))

# 5.
# word = input('Введите слово для поиска: ')
# with open('file1.txt', 'r', encoding='utf-8') as file_1:
#     text = file_1.read()
#     print(text.count(word))

# 6.
# word = input('Введите слово для замены: ')
# new_word = input('Введите слово для подмены: ')
#
# with open('file1.txt', 'r+', encoding='utf-8') as file_1:
#     text = file_1.read()
#     new_text = text.replace(word, new_word)
#     file_1.seek(0)
#     file_1.write(new_text)

# -------------------------------------------------------------

# Именование классов подчиняется концепции CamelCase
# class FloatNumber:
#     def __init__(self, num: int, denom: int) -> None:
#         self.numerator = num
#         self.denominator = denom
#
#     def add(self, other: 'FloatNumber'):
#         numerator = self.numerator * other.denominator + \
#                     other.numerator * self.denominator
#         denominator = self.denominator * other.denominator
#         return numerator, denominator
#
#
# a = FloatNumber(1, 2)
# b = FloatNumber(3, 4)
#
# print(a.add(b))


# Задание 1
# Реализуйте класс «Человек». Необходимо хранить в
# полях класса: ФИО, дату рождения, контактный телефон,
# город, страну, домашний адрес. Реализуйте методы класса
# для ввода данных, вывода данных.

# class Human:
#     def __init__(self, fio, dob, phone_number,
#                  city, country, adress):
#         self.fio = fio
#         self.dob = dob
#         self.phone_number = phone_number
#         self.city = city
#         self.country = country
#         self.adress = adress
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
#
# new_human = Human('Петров Василий Владимирович', '01.01.1970', '+79521412121',
#                   'Москва', 'Россия', 'Улица Пушкина, дом Колотушкина')
# new_human.print_info()
# new_human.reset()
# new_human.print_info()


# class A:
#     def __init__(self):
#         self.a = 5
#
#     def print(self):
#         print(self.a)
#
#
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         self.a = 3
#
# c = B()
# c.print()


# Задание 2.
# Напишите базовый класс Животное. В этом классе создайте свойство
# животных sound, которое хранит информацию о звуке, которое издаёт
# животное. Также создайте метод для издания звука(print)
# Сделайте несколько дочерних классов
# разных животных: Собака, Кошка, Попугай.
# Переопределите их конструкторы так, чтобы у каждого животного
# был свой звук.

# a = Animal()
# a.make_sound()
# >>> 'звук'
# d = Dog()
# d.make_sound()
# >>> 'гав-гав'
# c = Cat()
# c.make_sound()
# >>> 'мяяяу'
# p = Parrot()
# p.make_sound()
# >>> 'Попка дурак!'


# class Animal:
#     def __init__(self):
#         self.sound = 'sound'
#
#     def make_sound(self):
#         print(self.sound)
#
#
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         self.sound = 'Woof-woof'
#
#
# class Cat(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         self.sound = 'Meeoow'
#
#
# class Parrot(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         self.sound = 'Ничего на свете лучше нееетууу...'
#
#
# a = Animal()
# d = Dog()
# c = Cat()
# p = Parrot()
# a.make_sound()
# d.make_sound()
# c.make_sound()
# p.make_sound()


# Задание 3
# Создайте класс «Дробь». Необходимо хранить в полях
# класса: числитель и знаменатель.
# Реализуйте методы класса для ввода данных, вывода данных.
# Также создайте методы класса для выполнения арифметических
# операций (сложение, вычитание, умножение, деление).

# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.numerator = numerator
#         self.denominator = denominator
#
#     def input_data(self):
#         self.numerator = int(input("Введите числитель: "))
#         self.denominator = int(input("Введите знаменатель: "))
#
#     def display_data(self):
#         print(f"{self.numerator}/{self.denominator}")
#
#     def add(self, other):
#         result_numerator = self.numerator * other.denominator + self.denominator * other.numerator
#         result_denominator = self.denominator * other.denominator
#         return Fraction(result_numerator, result_denominator)
#
#     def subtract(self, other):
#         result_numerator = self.numerator * other.denominator - self.denominator * other.numerator
#         result_denominator = self.denominator * other.denominator
#         return Fraction(result_numerator, result_denominator)
#
#     def multiply(self, other):
#         result_numerator = self.numerator * other.numerator
#         result_denominator = self.denominator * other.denominator
#         return Fraction(result_numerator, result_denominator)
#
#     def divide(self, other):
#         result_numerator = self.numerator * other.denominator
#         result_denominator = self.denominator * other.numerator
#         return Fraction(result_numerator, result_denominator)
#
#
# fr1 = Fraction(3, 4)
# fr2 = Fraction(1, 2)
#
# result_add = fr1.add(fr2)
# result_add.display_data()
#
# result_subtract = fr1.subtract(fr2)
# result_subtract.display_data()
#
# result_multiply = fr1.multiply(fr2)
# result_multiply.display_data()
#
# result_divide = fr1.divide(fr2)
# result_divide.display_data()
