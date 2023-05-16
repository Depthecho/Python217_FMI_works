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
#             # Если список не пустой, перебираем и выводим все ноды
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
# a.show()
# a.show(reverse=True)



# 3.

# class Logger:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls, *args, **kwargs)
#             return cls._instance
#         else:
#             raise NotImplementedError('Нельзя создать больше одного логгера')
#
#     def __init__(self):
#         self.target = None
#         while self.target not in ['экран', 'файл']:
#             self.target = input('Введите, куда писать логи(экран/файл): ')
#         if self.target == 'файл':
#             self.filepath = input('Введите путь к файлу логов: ')
#             open(self.filepath, 'w').close()
#
#     def log_func(self, func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             log_message = f'Функция {func.__name__} была вызвана с аргументами {(*args, *kwargs.items())} ' \
#                           f'и вернула {result}'
#             if self.target == 'экран':
#                 print(log_message)
#             elif self.target == 'файл':
#                 with open(self.filepath, 'a', encoding='utf-8') as f:
#                     f.write('\n' + log_message)
#             return result
#         return wrapper
#
#
# logger = Logger()
#
#
# class Numbers:
#     def __init__(self):
#         self.numbers = list(map(int, input('Введите числа через пробел: ').split()))
#         self.work_file = input('Введите путь к файлу для работы: ')
#
#     @logger.log_func
#     def save(self):
#         with open(self.work_file, 'a') as f:
#             f.write('\n' + ' '.join(list(map(str, self.numbers))))
#
#     @logger.log_func
#     def find_min_max(self):
#         minimum, maximum = min(self.numbers), max(self.numbers)
#         with open(self.work_file, 'a') as f:
#             f.write('\n' + str(minimum) + ' ' + str(maximum))
#
#         return minimum, maximum
#
#     @logger.log_func
#     def print_numbers(self):
#         print(self.numbers)
#
#     @logger.log_func
#     def print_min_max(self):
#         print(min(self.numbers), max(self.numbers))
#
#
# numbers = Numbers()
#
# numbers.save()
# print(numbers.find_min_max())
# numbers.print_numbers()
# numbers.print_min_max()


# 2.

# from abc import ABC, abstractmethod
#
#
# class AbstractFactory(ABC):
#     @abstractmethod
#     def create_engine(self):
#         pass
#
#     @abstractmethod
#     def create_body(self):
#         pass
#
#
# class LuxuryCarFactory(AbstractFactory):
#     def create_engine(self):
#         return LuxuryEngine()
#
#     def create_body(self):
#         return LuxuryBody()
#
#
# class SportCarFactory(AbstractFactory):
#     def create_engine(self):
#         return SportEngine()
#
#     def create_body(self):
#         return SportBody()
#
#
# class LuxuryEngine:
#     def __str__(self):
#         return 'Luxury Engine'
#
#
# class LuxuryBody:
#     def __str__(self):
#         return 'Luxury Body'
#
#
# class SportEngine:
#     def __str__(self):
#         return 'Sport Engine'
#
#
# class SportBody:
#     def __str__(self):
#         return 'Sport Body'
#
#
# def main():
#     car_type = input('Input car type:\n'
#                      '1. luxury\n'
#                      '2. sport.\n')
#
#     if car_type == 'luxury':
#         car_factory = LuxuryCarFactory()
#     elif car_type == 'sport':
#         car_factory = SportCarFactory()
#     else:
#         raise ValueError(f'Wrong car type!')
#
#     engine = car_factory.create_engine()
#     body = car_factory.create_body()
#
#     print(f'Engine: {engine}')
#     print(f'Body: {body}')
#
#
# main()
