# Запрограммируйте класс Money (объект класс аоперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег(доллары,евро,гривны и т.д.) и поле для хранения
# копеек(центы, евроценты, копейки и т.д.).Реализовать методы для вывода суммы на экран,задания значений для частей

class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        return f"${self.dollars}.{self.cents}"

    def set_dollars(self, dollars):
        self.dollars = dollars

    def set_cents(self, cents):
        self.cents = cents

    def get_dollars(self):
        return self.dollars

    def get_cents(self):
        return self.cents

    def add(self, other):
        total_cents = self.cents + other.cents
        carry_over = total_cents // 100
        new_cents = total_cents % 100

        total_dollars = self.dollars + other.dollars + carry_over

        return Money(total_dollars, new_cents)

    def subtract(self, other):
        negative_other = Money(-other.dollars, -other.cents)
        return self.add(negative_other)


money1 = Money(50, 50)
money2 = Money(27, 25)
money3 = money1.add(money2)
print(money3)
money4 = money1.subtract(money2)
print(money4)
