# Создайте класс Complex (комплексное число)
# Создайте перегруженные операторы для реализации арифметических операций для по работе с комплексными числами
# (операции +, -, *, /).

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = Complex(7, 5)
c2 = Complex(4, -5)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)