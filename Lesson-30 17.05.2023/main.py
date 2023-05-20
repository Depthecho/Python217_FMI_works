# import json
# import pickle
#
#
# class Car:
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price
#
#     def to_pickle(self, filename):
#         with open(f'{filename}.pickle', 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def from_pickle(filename):
#         try:
#             with open(f'{filename}.pickle', 'rb') as f:
#                 return pickle.load(f)
#         except IOError as e:
#             print('Something went wrong,', e)
#             return None
#
#     def to_json(self, filename):
#         with open(f'{filename}.json', 'w') as f:
#             json.dump(self.__dict__, f)
#
#     @staticmethod
#     def from_json(filename):
#         with open(f'{filename}.json', 'r') as f:
#             properties = json.load(f)
#             return Car(properties['model'], properties['price'])
#
#
# car = Car('Toyota', 2000)
# car.to_json('car')
# new_car = Car.from_json('car')
# print(new_car.model, new_car.price)


# 1.

# class FileStrategy:
#     @staticmethod
#     def __out__(obj, value=None):
#         with open(obj.output_filename, 'a', encoding='utf-8') as f:
#             if value:
#                 f.write('\n' + str(value))
#             else:
#                 f.write('\n' + ' '.join(map(str, obj.arr)))
#
#     @staticmethod
#     def __in__(obj):
#         with open(obj.input_filename, 'r', encoding='utf-8') as f:
#             obj.arr = list(map(str, f.read().split()))
#
#
# class ConsoleStrategy:
#     @staticmethod
#     def __out__(obj, value=None):
#         if value:
#             print(value)
#         else:
#             print(*obj.arr)
#
#     @staticmethod
#     def __in__(obj):
#         obj.arr = list(map(int, input('Введите числа через пробел: ').split()))
#
#
# class Strategy:
#     def __init__(self):
#         self.arr = []
#         self.__strategy = None
#         self.input_filename = ''
#         self.output_filename = ''
#
#     @property
#     def strategy(self):
#         return self.__strategy
#
#     @strategy.setter
#     def strategy(self, value):
#         if value == 'файл':
#             self.__strategy = FileStrategy()
#             self.output_filename = input('Введите файл для вывода: ')
#             while True:
#                 self.input_filename = input('Введите файл для ввода: ')
#                 try:
#                     open(self.input_filename, 'r').close()
#                 except FileNotFoundError:
#                     print('Такого файла не существует!')
#                 else:
#                     break
#         elif value == 'экран':
#             self.__strategy = ConsoleStrategy()
#         else:
#             print('Неверно введена стратегия!')
#
#     def max(self):
#         self.strategy.__out__(self, max(self.arr))
#
#     def min(self):
#         self.strategy.__out__(self, min(self.arr))
#
#     def reverse(self):
#         self.arr.reverse()
#         self.strategy.__out__(self)
#
#     def write(self):
#         self.strategy.__out__(self)
#
#     def read(self):
#         self.strategy.__in__(self)
#
#
# a = Strategy()
# while True:
#     command = input('Введите номер команды:\n'
#                     '1. Считать данные\n'
#                     '2. Сохранить данные\n'
#                     '3. Найти максимум\n'
#                     '4. Найти минимум\n'
#                     '5. Перевернуть данные\n'
#                     '6. Установить стратегию.\n')
#     if command == '6':
#         a.strategy = input('Введите стратегию(файл/экран): ')
#     elif not a.strategy:
#         print('Сначала выберите стратегию!')
#     elif command == '1':
#         a.read()
#     elif command == '2':
#         a.write()
#     elif command == '3':
#         a.max()
#     elif command == '4':
#         a.min()
#     elif command == '5':
#         a.reverse()
#     else:
#         print('Такой команды не существует!')


# 2.
# import random
# import string
#
#
# class Student:
#     def __init__(self, name, age, group=None):
#         self.name = name
#         self.age = age
#         self.group = group
#
#     def __str__(self):
#         return f'{self.name}, {self.age}, {self.group}'
#
#
# class StudentGroup:
#     title = ''.join(random.sample(string.ascii_uppercase, 3))
#     number = 100
#
#     def __init__(self):
#         self.students = []
#         self.title = StudentGroup.title + str(StudentGroup.number)
#         StudentGroup.number += 1
#
#     def add_student(self, student):
#         self.students.append(student)
#         student.group = self
#
#     def __iter__(self):
#         self.index = 0
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.students):
#             raise StopIteration
#         student = self.students[self.index]
#         self.index += 1
#         return student
#
#     def __str__(self):
#         return self.title
#
#
# def show_all_groups():
#     for group in groups:
#         print(group.title)
#
# def show_all_students():
#     for student in students:
#         print(student)
#
# def show_group(group):
#     print(group.title)
#     for student in group:
#         print(student)
#
# def get_group(name):
#     for group in groups:
#         if group.title == name:
#             return group
#     return None
#
# def get_student(name):
#     for student in students:
#         if student.name == name:
#             return student
#     return None
#
#
# groups = []
# students = []

# while True:
#     command = input('Введите номер команды:\n'
#                     '1. Создать новую группу\n'
#                     '2. Удалить существующую группу\n'
#                     '3. Добавить нового студента\n'
#                     '4. Изменить данные о студенте\n'
#                     '5. Удалить студента из группы\n'
#                     '6. Просмотреть список всех групп\n'
#                     '7. Просмотреть список всех студентов\n'
#                     '0. Выйти')
#     if command == '0':
#         break
#     elif command == '1':
#         groups.append(StudentGroup())
#     elif command == '2':
#         show_all_groups()
#         group_name = input('Введите название группы для удаления: ')
#         group = get_group(group_name)
#         if group:
#             groups.remove(group)
#         else:
#             print('Такой группы нет!')
#     elif command == '3':
#         students.append(Student(input('Введите имя студента:'),
#                                 int(input('Введите возраст студента: ')),
#                                 input('Введите группу, в которую студент зачислен: ')))
#     elif command == '4':
#         student_name = input('Введите имя студента: ')
#         student = get_student(student_name)
#         student.name = input('Введите новое имя студента: ')
#         student.age = int(input('Введите новый возраст студента: '))
#         student.group = input('Введите новую группу студента: ')
#     elif command == '5':
#         student_name = input('Введите имя студента: ')
#         student = get_student(student_name)
#         for group in groups:
#             if student in group:
#                 group.students.remove(student)
#                 print(f'Студент: {student} был удален из группы {group}')
#     elif command == '6':
#         show_all_groups()
#     elif command == '7':
#         show_all_students()
#     else:
#         print('Такой команды нет!')
