# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
#
#     def __add__(self, other):
#         return Complex(self.real + other.real,
#                        self.imag + other.imag)
#
#     def __sub__(self, other):
#         return Complex(self.real - other.real,
#                        self.imag - other.imag)
#
#     def __mul__(self, other):
#         return Complex(self.real * other.real - self.imag * other.imag,
#                        self.real * other.imag + self.imag * other.real)
#
#     def __truediv__(self, other):
#         return Complex((self.real * other.real + self.imag * other.imag)
#                        / (other.real ** 2 + other.imag ** 2),
#                        (other.real * self.imag - self.real * other.imag)
#                        / (other.real ** 2 + other.imag ** 2))
#
#     def __str__(self):
#         return f'{self.real} + {self.imag}i'
#
#
# a = Complex(4, 2)
# b = Complex(2, 2)
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)


## Структуры данных
# 1. Связные списки(Односвязный и двусвязный)
# 2. Стек
# 3. Очередь, Приоритетная очередь


## Односвязный список
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = Node(value)
#
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#
#         current_node.next = new_node
#
#     def delete(self, value):
#         if self.head is None:
#             return
#
#         if self.head.value == value:
#             self.head = self.head.next
#             return
#
#         current_node = self.head
#         while current_node.next:
#             if current_node.next.value == value:
#                 current_node.next = current_node.next.next
#                 return
#             current_node = current_node.next
#
#     def show(self):
#         if self.head is None:
#             print('List is empty!')
#             return
#
#         current_node = self.head
#         while current_node:
#             print(current_node.value, end=' -> ')
#             current_node = current_node.next
#         print(None)
#
#
# a = LinkedList()
# a.append(2)
# a.append(4)
# a.append(3)
# a.show()
# a.delete(2)
# a.show()


## Двусвязный список
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None
#
#
# class BilinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         new_node = Node(value)
#
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#
#         current_node.next = new_node
#         current_node.next.prev = current_node
#
#     def delete(self, value):
#         if self.head is None:
#             return
#
#         if self.head.value == value:
#             self.head = self.head.next
#             self.head.prev = None
#             return
#
#         current_node = self.head
#         while current_node.next:
#             if current_node.next.value == value:
#                 current_node.next = current_node.next.next
#                 if current_node.next:
#                     current_node.next.prev = current_node
#                 return
#             current_node = current_node.next
#
#     def show(self):
#         if self.head is None:
#             print('List is empty!')
#             return
#
#         print(None, end=' <-> ')
#         current_node = self.head
#         while current_node:
#             print(current_node.value, end=' <-> ')
#             current_node = current_node.next
#         print(None)
#
#
# a = BilinkedList()
# a.append(2)
# a.append(4)
# a.append(3)
# a.show()
# a.delete(3)
# a.show()


# Стек(Произносится, как "стэк").
# Подчиняется правилу LIFO - Last In First Out
# class Stack:
#     def __init__(self):
#         self.lst = []
#
#     def push(self, value):
#         if not isinstance(value, int):
#             try:
#                 value = int(value)
#             except ValueError:
#                 print(f'Argument {value} is wrong data type!')
#             else:
#                 print(f'Warning! Your data type was reduced to int!! '
#                       f'And your value will be replaced with {value}')
#                 self.lst.append(value)
#         else:
#             self.lst.append(value)
#
#     def is_empty(self):
#         if len(self.lst) == 0:
#             return 'Stack is empty!'
#         return False
#
#     def pop(self):
#         return self.is_empty() or self.lst.pop()
#
#     def peek(self):
#         return self.is_empty() or self.lst[-1]
#
#     def clear(self):
#         self.lst.clear()
#         print('Stack is cleared!')
#
#     def length(self):
#         return len(self.lst)
#
#     def __str__(self):
#         return ' -> '.join(map(str, self.lst))
#
#
# stack = Stack()
# stack.push(5)
# stack.push(15.4)
# stack.push(0)
# stack.push(2)
# stack.push(17)
# print(stack)
# print(stack.pop())
# print(stack.peek())
# print(stack.is_empty())
# print(stack.length())


## Очередь - Queue
# Подчиняется правилу FIFO - First In First Out
class Queue:
    def __init__(self, size):
        self.lst = []
        self.size = size

    def is_empty(self):
        return len(self.lst) == 0

    def is_full(self):
        return len(self.lst) == self.size

    def enqueue(self, value):
        if self.is_full():
            print('Queue is full!')
        elif not isinstance(value, str):
            print(f'{value} is not a string!')
        else:
            self.lst.append(value)

    def dequeue(self):
        return self.lst.pop(0)

    def show(self):
        print(f' <- '.join(map(str, self.lst)))
#
#
# q = Queue(4)
# q.enqueue('1')
# q.enqueue('2')
# q.enqueue('3')
# q.enqueue('4')
# q.show()
# print(q.dequeue())
# q.show()
# q.enqueue('3')
# q.enqueue('4')


## Приоритетная очередь - Priority Queue
# Не подчиняется никакому из правил (LIFO/FIFO)
# class PriorityQueue(Queue):
#     def __init__(self, size):
#         Queue.__init__(self, size)
#
#     def enqueue(self, value):
#         """This method is deprecated"""
#         pass
#
#     def prior_insert(self, data):
#         if self.is_full():
#             return 'Queue is full!'
#
#         priority = data[1]
#         for i in range(len(self.lst)):
#             if priority > self.lst[i][1]:
#                 self.lst.insert(i, data)
#                 break
#         else:
#             self.lst.append(data)
#
#     def peek(self):
#         return self.lst[0][0]
#
#
# priority_queue = PriorityQueue(5)
# priority_queue.prior_insert(('Помыть посуду', 3))
# priority_queue.prior_insert(('Погулять с собакой', 7))
# priority_queue.prior_insert(('Сделать домашнее задание', 5))
# priority_queue.prior_insert(('Покушать', 10))
# priority_queue.show()
# print(priority_queue.dequeue())
# print(priority_queue.peek())
