# Итератор - это поведенческий паттерн, который предоставляет
# последовательный доступ к элементам объекта без раскрытия
# его базовой реализации

class MyClass:
    def __init__(self, lst):
        self.lst = lst
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i == len(self.lst):
            self.i = -1
            raise StopIteration
        result = self.lst[self.i]
        return result


a = MyClass([4, 2, 3, 4, 6])
for i in a:
    print(i)


# Метод, позволяющий получить буквы алфавита до конкретной,
# который возвращает итератор
# def alphabets_upto(letter):
#     for i in range(65, ord(letter) + 1):
#         yield chr(i)
#
#
# alphabets_upto_K = alphabets_upto('K')
# alphabets_upto_M = alphabets_upto('M')
#
# for alpha in alphabets_upto_K:
#     print(alpha, end=" ")
# print()
# for alpha in alphabets_upto_M:
#     print(alpha, end=" ")


# Использование встроенных генераторов для повторения поведения
# паттерна "итератор"
# def inBuilt_Iterator1():
#     alphabets = (chr(i) for i in range(65, 91))
#     for alpha in alphabets:
#         print(alpha, end=" ")
#     print()
#
#
# def inBuilt_Iterator2():
#     alphabets = [chr(i) for i in range(97, 123)]
#     for alpha in alphabets:
#         print(alpha, end=" ")
#     print()
#
#
# inBuilt_Iterator1()
# inBuilt_Iterator2()
