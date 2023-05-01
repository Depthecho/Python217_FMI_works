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
#         current_node.next = current_node.next.next
#
#     def show(self):
#         if self.head is None:
#             print(None)
#             return
#
#         current_node = self.head
#         while current_node:
#             print(current_node.value, end = '=>')
#             current_node = current_node.next
#             print(None)
#
#
# c = LinkedList()
# c.append(3)
# c.append(4)
# c.append(5)

# class Node:
#    def __init__(self, value):
#        self.value = value
#        self.next = None
#        self.prev = None
#
#
# class DoubleLinkedList:
#     def __init__(self):
#        self.head = None
#
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
#             current_node.next = current_node.next.nex
#
#     def show(self):
#         if self.head is None:
#             print('List is empty')
#             return
#
#         current_node = self.head
#         while current_node:
#             print(current_node.value, end='=>')
#             current_node = current_node.next
#             print(None)
#
#
# my_c = DoubleLinkedList()
# my_c.append(3)
# my_c.append(5)
# my_c.append(7)
# print(my_c.show())

# class Stack:
#     def __init__(self, size):
#         self.stack = []
#
#     def add(self, value):
#         if type(value) == int:
#             self.stack.append(value)
#         else:
#             raise Exception("Value's type is not int")
#
#     def delete(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         else:
#             raise Exception("Stack is emppty")
#
#     def count(self):
#         return len(self.stack)
#
#     def is_empty(self):
#         if len(self.stack) == 0:
#             return True
#         else:
#             return False
#
#     def clear(self):
#         self.stack.clear()
#
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#         else:
#             raise Exception("Stack is empty")

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def enqueue(self, value):
        if not self.is_full():
            self.queue.append(value)
        else:
            raise Exception("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise Exception("Queue is empty")

    def show(self, direction=''):
        print(f'-> {self.queue} ->')



