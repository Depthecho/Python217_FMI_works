class NumberList:
    def __init__(self, numbers: list):
        self.numbers = numbers

    # Функция подсчёта суммы всех элементов набора:
    def sum(self):
        return sum(self.numbers)

    # Функция на нахождение среднего арифметического из элементов набора:
    def average(self):
        return sum(self.numbers) / len(self.numbers)

    # Функция нахождения максимума из элементов набора:
    def maximum(self):
        return max(self.numbers)

    # Функция на нахождение минимума из элемента набора:
    def minimum(self):
        return min(self.numbers)
