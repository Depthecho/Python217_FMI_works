# SOLID - пять принципов дизайна
# создания классовой архитектуры

# 1. S - Single Responsibility - Единственная ответственность
# Принцип единственной ответственности - у объекта экземпляра
# класса должна быть только одна обязанность, решение которой
# полностью входит в тело класса

# Плохой пример создания и организации классов
# class Library:
#     def add_new_reader(self):
#         pass
#
#     def add_new_book(self):
#         pass
#
#     def reset_book_property(self):
#         pass
#
#     def add_new_librarian(self):
#         pass

# Простой пример использования принципа единственной ответственности
# class Reader:
#     pass
#
# class Book:
#     pass
#
# class Librarian:
#     pass
#
# class Library:
#     def add_new_reader(self):
#         return Reader()

# 2. O - Open - Closed
# Принцип открытости/закрытости - программируемые сущности(классы,
# функции, модули) должны быть открыты для расширения, но закрыты
# для модификации.

# Плохой пример
# class Discount:
#     def __init__(self, price):
#         self.price = price
#
#     def give_discount(self, status):
#         if status == 1:
#             return self.price * (1 - 0.05)
#         elif status == 2:
#             return self.price * (1 - 0.1)
#         elif status == 3:
#             return self.price * (1 - 0.15)

# class Discount:
#     def __init__(self, price):
#         self.price = price
#
#     def get_discount(self):
#         pass
#
# class DiscountLevel1(Discount):
#     def get_discount(self):
#         return self.price * (1 - 0.05)
#
# class DiscountLevel2(Discount):
#     def get_discount(self):
#         return self.price * (1 - 0.1)
#
# class DiscountLevel3(Discount):
#     def get_discount(self):
#         return self.price * (1 - 0.15)


# 3. L - Liskov substitution principle
# Принцип подстановки Барбары Лисков - сущности, которые используют
# базовый тип данных, должны иметь возможность использовать подтипы
# базового типа, не зная об этом

# class IntegerNumber:
#     def __init__(self, value):
#         self.value = int(value)
#
#     def __str__(self):
#         return f'{self.value}'
#
#
# class FloatNumber(IntegerNumber):
#     def __init__(self, value):
#         self.value = value
#
#
# def multiply_string(string, num: IntegerNumber):
#     try:
#         return string * num.value
#     except TypeError as e:
#         if isinstance(num.value, float):
#             return string * int(num.value)
#
#
# a = IntegerNumber(5.5)
# b = FloatNumber(5.5)
# print(multiply_string('Hi', a))
# print(multiply_string('Hi', b))


# 4. I - Interface Substitution Principle
# Принцип разделения интерфейса - клиенты не должны зависеть
# от функции, которые они не используют


# Плохой пример
# from abc import ABC, abstractmethod
#
# class Phone(ABC):
#
#     @abstractmethod
#     def make_call(self):
#         pass
#
#     @abstractmethod
#     def send_sms(self):
#         pass
#
#     @abstractmethod
#     def browse_internet(self):
#         pass
#
#
# class SmartPhone(Phone):
#     def make_call(self):
#         pass
#
#     def send_sms(self):
#         pass
#
#     def browse_internet(self):
#         pass
#
#
# class OldPhone(Phone):
#
#     def make_call(self):
#         pass
#
#     def send_sms(self):
#         pass
#
#     def browse_internet(self):
#         raise NotImplementedError


# Хороший пример, соблюдающий принцип
# from abc import ABC, abstractmethod
#
#
# class CallingDevice(ABC):
#     @abstractmethod
#     def make_call(self):
#         pass
#
#
# class MessagingDevice(ABC):
#     @abstractmethod
#     def send_sms(self):
#         pass
#
#
# class BrowsingInternetDevice(ABC):
#     @abstractmethod
#     def browse_internet(self):
#         pass
#
#
# class SmartPhone(CallingDevice, MessagingDevice, BrowsingInternetDevice):
#     def make_call(self):
#         pass
#
#     def send_sms(self):
#         pass
#
#     def browse_internet(self):
#         pass
#
#
# class OldPhone(CallingDevice, MessagingDevice):
#     def make_call(self):
#         pass
#
#     def send_sms(self):
#         pass


# 5. D - Dependency Inversion Principle
# Принцип инверсии зависимостей - модули верхних уровней
# не должны зависеть от модулей нижних уровней. А оба типа
# модулей должны зависеть от абстракций. Сами абстракции
# не должны зависеть от деталей реализации, но детали
# реализации должны зависеть от абстракций.

# class Payment:
#     def do_transaction(self, amount):
#         raise NotImplementedError
#
#
# class Cash(Payment):
#     def do_transaction(self, amount):
#         pass
#
#
# class BankCard(Payment):
#     def do_transaction(self, amount):
#         pass
#
#
# class ApplePay(Payment):
#     def do_transaction(self, amount):
#         pass
#
#
# class Shop:
#     def do_payment(self, payment, amount):
#         payment.do_transaction(amount)

