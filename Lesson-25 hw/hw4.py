# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# Проверка на равенство площадей квартир (операция ==);
# Проверка на неравенство площадей квартир (операция !=);
# Сравнение двухк вартир по цене (операции >, <, <=, >=).

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price


f1 = Flat(95, 12000000)
f2 = Flat(70, 9500000)
print(f1 == f2)
print(f1 != f2)
print(f1 > f2)
print(f1 < f2)
print(f1 >= f2)
print(f1 <= f2)