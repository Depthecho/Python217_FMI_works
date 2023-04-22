# Создайте класс Circle(окружность). Для данного класса реализ уйте ряд перегруженных операторов:
# Проверка на равенство радиусов двух окружностей (операция ==);
# Сравнения длин двух окружностей (операции >, <, <=,>=);
# Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции +, -, +=, -=)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __isub__(self, other):
        self.radius -= other.radius
        return self


c1 = Circle(7)
c2 = Circle(7)
c3 = Circle(15)

print(c1 == c2)
print(c1 == c3)

print(c1 <= c2)
print(c1 > c3)

c1 += c2
print(c1.radius)

c3 -= c1
print(c3.radius)
