# Вкратце, цель шаблона Singleton заключаются в следующем:
# • Обеспечение создания одного и только одного объекта класса
# • Контроль одновременного доступа к ресурсам, которые являются общим
import sys


class Singleton:
    def __new__(cls, width, height):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        else:
            print(f'You are resetting {cls.__name__} object attributes', file=sys.stderr)
            sys.stderr.flush()
        cls.__init__(cls._instance, width, height)
        return cls._instance

    def __init__(self, width, height):
        self.width = width
        self.height = height


class New(Singleton):
    pass


a = New(2, 5)
print(a.width, a.height)
b = New(3, 4)
print(a.width, a.height)
print(id(a))
print(id(b))
print(a is b)
