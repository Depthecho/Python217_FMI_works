# class Node:
#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next
#
#
# class DoubleLinkedList:
#     def __init__(self, lst=None):
#         self.head = None
#         self.tail = None
#         if lst:
#             for value in lst[1:]:
#                 self.append(value, unique=False)
#
#     def append(self, value, unique=True):
#         if unique and self.is_there(value):
#             print('Это значение уже существует в списке!!')
#             return
#         new_node = Node(value)
#
#         # Если список пустой, делаем новую ноду головой
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#
#         # Если список не пустой, перебираем все ноды, пока не дойдём
#         # до последней
#         current_node = self.head
#         while current_node.next is not None:
#             current_node = current_node.next
#
#         # Добавляем нашу ноду в next последней, делая её новой последней
#         current_node.next = new_node
#         new_node.prev = current_node
#         self.tail = new_node
#
#     def delete(self, value):
#         # Если список пустой, ничего не делаем, отдыхаем
#         if self.head is None:
#             return
#
#         # Если то, что мы хотим удалить, это голова, то удаляем её
#         if self.head.value == value:
#             self.head = self.head.next
#             if self.head is not None:
#                 self.head.prev = None
#             else:
#                 self.tail = None
#             return
#
#         # Если список не пустой, перебираем все ноды, пока не дойдём
#         # до искомого value или до конца списка
#         current_node = self.head
#         while current_node.next is not None:
#             if current_node.next.value == value:
#                 current_node.next = current_node.next.next
#                 if current_node.next is not None:
#                     current_node.next.prev = current_node
#             else:
#                 current_node = current_node.next
#         self.tail = current_node
#
#     def replace(self, old_value, new_value, all=False):
#         if self.head is None:
#             return
#
#         if self.head.value == old_value:
#             self.head.value = new_value
#             if not all:
#                 return
#
#         current_node = self.head
#         while current_node is not None:
#             if current_node.value == old_value:
#                 current_node.value = new_value
#                 if not all:
#                     return
#             current_node = current_node.next
#
#     def is_there(self, value):
#         if self.head is None:
#             return False
#
#         if self.head.value == value:
#             return True
#
#         current_node = self.head
#         while current_node.next is not None:
#             if current_node.next.value == value:
#                 return True
#             current_node = current_node.next
#         return False
#
#     def show(self, reverse=False):
#         # Если список пустой, выводим сообщение об этом
#         if self.head is None:
#             print('List is empty!')
#             return
#         print('None', end=' <-> ')
#         if reverse:
#             current_node = self.tail
#             while current_node is not None:
#                 print(current_node.value, end=' <-> ')
#                 current_node = current_node.prev
#         else:
#             current_node = self.head
#             while current_node is not None:
#                 print(current_node.value, end=' <-> ')
#                 current_node = current_node.next
#         print('None')
#
#
# a = DoubleLinkedList(lst=[5, 4, 3, 2, 1, 1, 1])
# a.show()
# a.replace(1, 5, all=True)
# a.delete(2)
# a.show()
# a.show(reverse=True)
# Сериализация - это процесс перевода значения структуры данных в битовую последовательность
# Десериализация - это процесс, обратный сериализации

# import pickle
#
# lst = [1, 2, 3, 'Hello', [0, 0], (1, 1)]
#
#
# class MyNumber:
#     def __init__(self, value):
#         self.value = value
#         self.positive = self.value >= 0


# a = MyNumber(6)
# with open('file.txt', 'wb') as f:
#     pickle.dump(a, f)
#
# with open('file.txt', 'rb') as f:
#     new_a = pickle.load(f)
#
# print(new_a)
# print(a.value == new_a.value)
# print(a.positive == new_a.positive)


# lst_str = pickle.dumps(lst)
#
# print(lst_str)
# new_lst = pickle.loads(lst_str)
#
# print(lst == new_lst)
# print(new_lst)


## JSON - JavaScript Object Notation - формат хранения данных наподобие того, как объекты
## хранятся в JavaScript
## {'x': 0, 'y': 5}

# import json
#
#
# class MyNumber:
#     def __init__(self, value, positive=None):
#         self.value = value
#         self.positive = self.value >= 0 if not positive else positive
#
#
# a = MyNumber(6)
# b = MyNumber(-4)
# c = MyNumber(0)
# d = MyNumber(0)
# objects = [a, b, c, d]
# with open('file.txt', 'w') as f:
#     json.dump({f'{obj.__class__.__name__} {i}': obj.__dict__ for i, obj in enumerate(objects)}, f)

## eval() - функция, которая принимает некоторую строку и "выполняет" её с помощью интерпретатора
## Python. А результат выполнения возвращает
## REPL - Read Evaluate Print - Loop (в грубом переводе: Прочти, Выполни, Верни результат, Повтори)

# with open('file.txt', 'r') as f:
#     new_a = json.load(f)
#
# new_lst = []
# for i in range(len(new_a)):
#     name_class = list(new_a.keys())[i].split()[0]
#     obj_prop = list(new_a.values())[i]
#     new_obj = globals()[name_class](**obj_prop)
#     new_lst.append(new_obj)
#
# print(new_lst)

# Методы loads и dumps являются аналогами для
# работы со строковым типом данных вместо файлов

# import json
#
# my_dict = {"1": "name", "2": "new"}
# print(json.loads(my_dict))
# print(json.dumps(my_dict))


# 1 и 2 задания

# import pickle
# import json
#
#
# class Plane:
#     def __init__(self, model, capacity, dimensions, id):
#         self.model = model
#         self.capacity = capacity
#         self.dimensions = dimensions
#         self.id = id
#
#     def takeoff(self):
#         print(f'The Plane {self.model} is taking off...')
#
#     def land(self):
#         print(f'The Plane {self.model} is landing...')
#
#     def save_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def load_pickle(filename):
#         try:
#             with open(filename, 'rb') as f:
#                 return pickle.load(f)
#         except FileNotFoundError:
#             print('Incorrect filepath provided!')
#
#     def save_json(self, filename):
#         with open(filename, 'w') as f:
#             json.dump(self.__dict__, f)
#
#     @staticmethod
#     def load_json(filename):
#         with open(filename, 'r') as f:
#             plane_dict = json.load(f)
#             return Plane(**plane_dict)
#
#     def __str__(self):
#         return f'Model: {self.model}\n' \
#                f'Capacity: {self.capacity}\n' \
#                f'Width: {self.dimensions[0]}\n' \
#                f'Length: {self.dimensions[1]}'


# a = Plane('Boeing 777', 300, (50, 200), '1415')
# print(a)
# a.save_pickle('plane.txt')
# new_plane = Plane.load_pickle('plane.txt')
# print(new_plane)
# new_plane.takeoff()
# new_plane.land()

# b = Plane('Boeing 737', 200, (40, 160), '6235')
# b.save_json('plane.json')
# new_b = Plane.load_json('plane.json')
# print(new_b)
# new_b.takeoff()
# new_b.land()


# CSV - Comma Separated Values - Значения, разделенные запятой

# import csv
#
# lst = [[[i, j] for i in range(10)] for j in range(10)]
#
# with open('file.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(lst)
#
# reader = csv.reader(open('file.csv', 'r'))
# for i in reader:
#     print(i)

