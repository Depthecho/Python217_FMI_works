# 1. Функциональная реализация

# Стратегия вывода на экран
def console_writer(info):
    print(info)

# Стратегия вывода в файл
def file_writer(info):
    with open('log.txt', 'a') as file:
        file.write(info + '\n')

# Интерфейс, работающий со стратегией
def client(writer):
    writer('Hello world!')
    writer('Good bye!')

# Код, где пользователь выбирает стратегию
if input('Записывать в файл?').lower() == 'да':
    client(writer=file_writer)
else:
    client(writer=console_writer)

# Стратегия выбирается пользователем, а функция
# client даже не знает, какой вариант алгоритма
# ей дадут. Она знает лишь то, что writer(info)
# – это некая функция, принимающая строку
# (это и есть общий интерфейс для всех стратегий).
# Таким образом, мы делегируем работу стратегиям,
# скрывая детали реализации каждой из них.


# 2. Объектная реализация

from abc import ABC, abstractmethod

# Определение общего поведения стратегий
class BaseStrategy(ABC):
    @abstractmethod
    def do_work(self, x, y):
        pass

# Стратегия 1
class Adder(BaseStrategy):
    def do_work(self, x, y):
        return x + y

# Стратегия 2
class Multiplicator(BaseStrategy):
    def do_work(self, x, y):
        return x * y

# Интерфейс, работающий со стратегией
class Calculator:
    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    def calculate(self, x, y):
        print('Result is', self.strategy.do_work(x, y))


calc = Calculator()
if input('Вы хотите сложить или умножить числа?').lower() == 'сложить':
    calc.set_strategy(Adder())
else:
    calc.set_strategy(Multiplicator())
x, y = input('Введите первое число: '), input('Введите второе число: ')
calc.calculate(int(x), int(y))
