from abc import ABC, abstractmethod
import json

class Pizza(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__('Margarita', 5)

class FourCheesePizza(Pizza):
    def __init__(self):
        super().__init__('Four Cheese', 8)

class HawaiianPizza(Pizza):
    def __init__(self):
        super().__init__('Hawaiian', 6)

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__('Pepperoni', 7)

class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__('Veggie', 4)

class Topping(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price


class CheeseTopping(Topping):
    def __init__(self):
        super().__init__('Cheese', 0.20)

class VegetableTopping(Topping):
    def __init__(self):
        super().__init__('Vegetable', 0.07)

class ChileTopping(Topping):
    def __init__(self):
        super().__init__('Chile', 0.15)

class PineappleTopping(Topping):
    def __init__(self):
        super().__init__('Pineapple', 0.1)

class SweetBowTopping(Topping):
    def __init__(self):
        super().__init__('Sweet Bow', 0.1)


class PizzaBuilder:
    def __init__(self):
        self._pizza = None

    def set_pizza(self, pizza):
        self._pizza = pizza
        return self

    def add_topping(self, topping):
        self._pizza = ToppedPizza(self._pizza, topping)
        return self

class ToppedPizza(Pizza):
    def __init__(self, pizza, topping):
        self._pizza = pizza
        self._topping = topping

    @property
    def name(self):
        return self._topping.name + ' ' + self._pizza.name

    @property
    def price(self):
        return self._pizza.price + self._topping.price

def pizza_factory(pizza_type):
    if pizza_type == 'Margarita':
        return MargaritaPizza()
    if pizza_type == 'Four Cheese':
        return FourCheesePizza()
    if pizza_type == 'Hawaiian':
        return HawaiianPizza()
    if pizza_type == 'Pepperoni':
        return PepperoniPizza()
    if pizza_type == 'Veggie':
        return VeggiePizza()

def topping_factory(topping_type):
    if topping_type == 'Cheese':
        return CheeseTopping()
    if topping_type == 'Vegetable':
        return VegetableTopping()
    if topping_type == 'Chile':
        return ChileTopping()
    if topping_type == 'Pineapple':
        return PineappleTopping()
    if topping_type == 'Sweet Bow':
        return SweetBowTopping()


class Logger:
    def __init__(self, filename='log.json'):
        self._filename = filename

    def log_order(self, order):
        print(f'Order details: {order}')
        with open(self._filename, 'a') as f:
            json.dump(order, f)
            f.write('\n')

class Payment(ABC):
    @abstractmethod
    def make_transaction(self)
        pass
class Cash(Payment):
    pass
class BankCard(Payment):
    pass
class FinancialCondition(Pizza):
    def __init__(self, number_of_pizzas_sold, revenue, profit):
        self.number_of_pizzas_sold = number_of_pizzas_sold
        self.revenue = revenue
        self.profit = profit






