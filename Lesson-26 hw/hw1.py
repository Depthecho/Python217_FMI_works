# Создать базовый класс Фигура с методом для подсчета площади. Создать производные классы :прямоугольник, круг,
# прямоугольный треугольник, трапеция со своими методами для подсчета площади

import math


class Figure:
    def area(self):
        pass


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
print(my_rect.area())

my_circ = Circle(7)
print(my_circ.area())

my_tri = RightTriangle(6, 12)
print(my_tri.area())

my_trap = Trapezoid(10, 6, 8)
print(my_trap.area())
