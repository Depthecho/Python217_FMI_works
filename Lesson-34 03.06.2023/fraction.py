class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        lcm = self.denominator * other.denominator
        numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Fraction(numerator, lcm)

    def __sub__(self, other):
        lcm = self.denominator * other.denominator
        numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        return Fraction(numerator, lcm)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)
