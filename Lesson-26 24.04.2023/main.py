# class Money:
#     def __init__(self, main_currency, assist_currency):
#         self.__main_currency = main_currency
#         self.__assist_currency = assist_currency
#
#     @property
#     def main_currency(self):
#         return self.__main_currency
#
#     @main_currency.setter
#     def main_currency(self, value):
#         self.__main_currency = value
#
#     @property
#     def assist_currency(self):
#         return self.__assist_currency
#
#     @assist_currency.setter
#     def assist_currency(self, value):
#         self.__assist_currency = value
#
#     def __str__(self):
#         return f'{self.main_currency}.{self.assist_currency}'
#
#     def add(self, other):
#         assist = self.assist_currency + other.assist_currency
#         return Money(self.main_currency + other.main_currency + assist // 100,
#                      assist % 100)
#
#
# a = Money(10, 50)
# b = Money(15, 76)
# print(a, b)
# print(a.add(b))
# a.main_currency = 20
# print(a)


# Множественное наследование vs Композиция
# class A:
#     def __init__(self, a):
#         self.a = a
#
#
# class B:
#     def __init__(self, b):
#         self.b = b
#
#
# class C(A, B):
#     def __init__(self, value):
#         A.__init__(self, value)
#         B.__init__(self, value)


# class A:
#     def __init__(self, a):
#         self.a = a
#
#
# class B:
#     def __init__(self, b):
#         self.b = b
#
#
# class C:
#     def __init__(self, value):
#         self.obj_A = A(value)
#         self.obj_B = B(value)
#
#
# c = C(3)
# print(c.obj_B.b)
# print(c.obj_A.a)


# 1.

# Реализуйте два класса: Окружность и Квадрат. У них должно
# быть по одному атрибуту, соответственно, радиус и длина стороны.
# Также должно быть обязательное свойство(property) площадь, которое
# возвращает площадь фигур. Затем создайте 3-ий класс, который
# наследуется от первых двух и при создании объекта этого класса
# принимает в конструктор экземпляры двух основных классов. Затем
# проверяет можно ли эту окружность вписать в этот квадрат. Если
# можно, то создаём объект, если нельзя, то кидаем исключение
# Также у этого объекта должно быть своё свойство(property) - площадь
# которая равна Sкв - Sкр.


# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     @property
#     def area(self):
#         return self.r ** 2 * 3.14
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     @property
#     def area(self):
#         return self.a ** 2
#
#
# class CircleInSquare:
#     def __init__(self, circle, square):
#         self.circle = circle
#         self.square = square
#         if circle.r * 2 != square.a:
#             raise ValueError('Нельзя вписать эту окружность в этот квадрат')
#
#     @property
#     def area(self):
#         return self.square.a ** 2 - self.circle.r ** 2 * 3.14
#
#
# a = Circle(5)
# b = Square(10)
# print(a.area)
# print(b.area)
# c = CircleInSquare(a, b)
# print(c.area)
# print(c.circle.r, c.square.a)


# 3.

# class Wheel:
#     def __init__(self, size):
#         self.size = size
#
#
# class Engine:
#     def __init__(self, horsepower):
#         self.horsepower = horsepower
#
#
# class Carcase:
#     def __init__(self, type, color):
#         self.type = type
#         self.color = color
#
#
# class Doors:
#     def __init__(self, direction):
#         self.direction = direction
#
#
# class Car(Wheel, Engine, Carcase, Doors):
#     def __init__(self, *args):
#         current = 0
#         for cls in Car.__bases__:
#             count_args = cls.__init__.__code__.co_argcount - 1
#             cls.__init__(self, *args[current: current + count_args])
#             current += count_args
#
#
# car = Car(30, 200, 'Седан', 'Зелёный', 'Наверх')
# print(car.size)
# print(car.horsepower)
# print(car.type)
# print(car.color)
# print(car.direction)


## Вызываемый объект(aka Функция)
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     def __call__(self, *args, **kwargs):
#         print(args)
#         for key, value in kwargs.items():
#             print(key, value)
#
#
# a = MyClass(5)
# a(14, 22, 'new', data=[1, 2, 3], end='15')


# 3.

# class DomesticAnimal:
#     def __init__(self, sound_text, name, species):
#         self.sound_text = sound_text
#         self.name = name
#         self.species = species
#
#     def sound(self):
#         print(self.sound_text)
#
#         def show(self):
#             print(self.name)
#
#         def type(self):
#             print(self.species)
#
#
#     class Dog(DomesticAnimal):
#         def __init__(self, name):
#             DomesticAnimal.__init__(self, 'Woof', name, 'Собака')
#
#
#     class Cat(DomesticAnimal):
#         def __init__(self, name):
#             DomesticAnimal.__init__(self, 'Meow', name, 'Кошка')
#
#
#     class Parrot(DomesticAnimal):
#         def __init__(self, name):
#             DomesticAnimal.__init__(self, "I'm smart!", name, 'Попугай')
#
#
#     class Hamster(DomesticAnimal):
#         def __init__(self, name):
#             DomesticAnimal.__init__(self, 'Peep-peep', name, 'Хомяк')
#
#
#     cat = Cat('Мурзик')
#     dog = Dog('Тузик')
#     parrot = Parrot('Кеша')
#     hamster = Hamster('Джонни')
#     animals = [cat, dog, parrot, hamster]
#
#     for animal in animals:
#         animal.show()
#         animal.type()
#         animal.sound()
#         print('-----------------')


# 4.

# class Employee:
#     def __init__(self, department, cabinet, name, age, position, salary):
#         self.department = department
#         self.cabinet = cabinet
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary
#
#     def print(self):
#         print(f'This is {self.name}. He is {self.age}. \nHe works at the {self.department} '
#               f'as {self.position} and he got paid about {self.salary} '
#               f'monthly. \nYou can find him at the {self.cabinet} cabinet.')
#
#     def __str__(self):
#         return f'{self.name}, {self.position}'
#
#     def __int__(self):
#         return int(self.age)
#
#
# class President(Employee):
#     def __init__(self, name, age, salary, schedule):
#         Employee.__init__(self, "president's department", '123', name,
#                           age, 'president', salary)
#         self.schedule = schedule
#
#     def make_an_appointment(self, day_of_week):
#         if day_of_week in self.schedule:
#             print(f'You made an appointment with Mr. President on {day_of_week}')
#         else:
#             print(f"Sorry, Mr. President not available at this day: {day_of_week}")
#
#
# class Manager(Employee):
#     def __init__(self, department, cabinet, name, age, salary):
#         Employee.__init__(self, department, cabinet, name,
#                           age, 'manager', salary)
#         self.stress = 0
#
#     def order_others_to_work(self):
#         if self.stress < 7:
#             print('Hey everyone! Work!')
#         else:
#             print("I'm to tired for this...")


