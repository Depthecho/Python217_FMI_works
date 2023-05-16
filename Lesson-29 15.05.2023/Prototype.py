# Шаблон проектирования Prototype решает проблему
# копирования объектов путем делегирования этой
# задачи самим объектам. Все объекты, которые
# можно копировать, должны реализовать метод
# clone и использовать его для получения
# точных копий самих себя.

from abc import ABC, abstractmethod


class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class MyObject(Prototype):
    def __init__(self, arg1, arg2):
        self.field1 = arg1
        self.field2 = arg2
        self.performed_operation = False

    def __operation__(self):
        self.performed_operation = True

    def clone(self):
        obj = MyObject(self.field1, self.field2)
        obj.performed_operation = self.performed_operation
        return obj


# Шаблон Prototype может быть действительно полезен в
# крупномасштабных приложениях, которые создают
# множество объектов. Иногда копирование уже
# существующего объекта обходится дешевле,
# чем создание нового.
