# Для классов из задания 1 нужно переопределить магические методы int (возвращает площадь)
# и str (возвращает информацию о фигуре)

class Figure:
    def area(self):
        pass

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Площадь фигуры '{self.__class__.__name__}' составляет {self.area()} см"


class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return ((self.base1 + self.base2) * self.height) / 2


my_rect = Rectangle(7, 15)
print(int(my_rect))
print(str(my_rect))

my_circ = Circle(7)
print(int(my_circ))
print(str(my_circ))

my_tri = RightTriangle(6, 12)
print(int(my_tri))
print(str(my_tri))

my_trap = Trapezoid(10, 6, 8)
print(int(my_trap))
print(str(my_trap))