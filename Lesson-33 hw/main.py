from abc import ABC, abstractmethod

# Абстрактный класс Pizza
class Pizza(ABC):
    def __init__(self, name, price, ingredient_cost):
        self.name = name
        self.price = price
        self.ingredient_cost = ingredient_cost

    @abstractmethod
    def calculate_profit(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Классы пицц наследующиеся от класса Pizza
class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita", 10, 5)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__("Pepperoni", 12, 6)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


class HawaiianPizza(Pizza):
    def __init__(self):
        super().__init__("Hawaiian", 14, 7)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


class FourCheesePizza(Pizza):
    def __init__(self):
        super().__init__("FourCheese", 16, 8)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


class VeggiePizza(Pizza):
    def __init__(self):
        super().__init__("Veggie", 10, 5)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


# Абстрактный класс Topping
class Topping(ABC):
    def __init__(self, name, price, ingredient_cost):
        self.name = name
        self.price = price
        self.ingredient_cost = ingredient_cost

    @abstractmethod
    def calculate_profit(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Классы топпингов наследующиеся от класса Topping
class CheeseTopping(Topping):
    def __init__(self):
        super().__init__('Cheese', 0.20, 0.10)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


class VegetableTopping(Topping):
    def __init__(self):
        super().__init__('Vegetable', 0.07, 0.03)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


class ChileTopping(Topping):
    def __init__(self):
        super().__init__('Chile', 0.15, 0.07)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


class PineappleTopping(Topping):
    def __init__(self):
        super().__init__('Pineapple', 0.2, 0.1)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


class SweetBowTopping(Topping):
    def __init__(self):
        super().__init__('Sweet Bow', 0.1, 0.05)

    def calculate_profit(self):
        return self.price - self.ingredient_cost

    def __str__(self):
        return self.name


# Класс для создания комбинированной пиццы
class PizzaBuilder:
    def __init__(self):
        self.pizza = None

    def set_pizza(self, pizza):
        self.pizza = pizza

    def add_topping(self, topping):
        self.pizza.price += topping.price
        self.pizza.ingredient_cost += topping.ingredient_cost

    def build(self):
        return self.pizza


# Класс Logger для записи заказов в файл и вывода на экран:
class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.user_id = 0

    def log_order(self, order):
        self.user_id += 1
        with open(self.filename, "a") as file:
            file.write(str(f'User {self.user_id} ordered: {order} pizza.') + "\n")
        print(f"User {self.user_id} ordered:", order, "pizza")


# Класс Pizzeria для создания заказов и расчета финансовых показателей
class Pizzeria:
    def __init__(self):
        self.orders = []
        self.logger = Logger("orders.log")

    def create_pizza(self, pizza, toppings=None):
        builder = PizzaBuilder()
        builder.set_pizza(pizza)

        if toppings:
            for topping in toppings:
                builder.add_topping(topping)

        new_pizza = builder.build()
        self.orders.append(new_pizza)
        self.logger.log_order(new_pizza)

    # Счётчик доходов
    def calculate_income(self):
        total_income = sum(pizza.price for pizza in self.orders)
        return total_income

    # Счётчик расходов
    def calculate_expenses(self):
        total_expenses = sum(pizza.ingredient_cost for pizza in self.orders)
        return total_expenses

    # Счётчик выручки
    def calculate_revenue(self):
        total_revenue = self.calculate_income() - self.calculate_expenses()
        return total_revenue


# Функция для работы с пользователем через меню
def main_pizzeria():
    password = '34556163'
    pizzeria = Pizzeria()
    while True:
        user_order = input("Welcome to our pizzeria !\n"
                           "We have 5 pizzas: 'Margherita', 'Pepperoni', 'Hawaiian', 'FourCheese' and 'Veggie'\n"
                           "For exit u need type 'exit'\n"
                           "For develop console type 'dc'\n"
                           "Do you want to make an order? (Yes/No): ")
        if user_order.lower() == 'no':
            break
        elif user_order.lower() == 'yes':
            user_pizza_selection = input('Enter the name of the pizza you want to order: ')
            if user_pizza_selection.lower() == 'margherita':
                margherita_pizza = MargheritaPizza()
                offer_topping = input("The same we have 5 toppings: 'Cheese', 'Vegetable', 'Chile', 'Pineapple', "
                                      "'Sweet bow'\n"
                                      "Do you want to add topping? (Yes/No): ")
                if offer_topping.lower() == 'no':
                    pizzeria.create_pizza(margherita_pizza)
                elif offer_topping.lower() == 'yes':
                    user_topping_selection = input("Enter the name of the topping you want to add: ")
                    if user_topping_selection.lower() == 'cheese':
                        cheese_topping = CheeseTopping()
                        pizzeria.create_pizza(margherita_pizza, [cheese_topping])
                    elif user_topping_selection.lower() == 'vegetable':
                        vegetable_topping = VegetableTopping()
                        pizzeria.create_pizza(margherita_pizza, [vegetable_topping])
                    elif user_topping_selection.lower() == 'chile':
                        chile_topping = ChileTopping()
                        pizzeria.create_pizza(margherita_pizza, [chile_topping])
                    elif user_topping_selection.lower() == 'pineapple':
                        pineapple_topping = CheeseTopping()
                        pizzeria.create_pizza(margherita_pizza, [pineapple_topping])
                    elif user_topping_selection.lower() == 'sweet bow':
                        sweetbow_topping = SweetBowTopping()
                        pizzeria.create_pizza(margherita_pizza, [sweetbow_topping])
                    else:
                        print("We don't have this topping")
                else:
                    print("Wrong answer")
            elif user_pizza_selection.lower() == 'pepperoni':
                pepperoni_pizza = PepperoniPizza()
                offer_topping = input("The same we have 5 toppings: 'Cheese', 'Vegetable', 'Chile', 'Pineapple', "
                                      "'Sweet bow'\n"
                                      "Do you want to add topping? (Yes/No): ")
                if offer_topping.lower() == 'no':
                    pizzeria.create_pizza(pepperoni_pizza)
                elif offer_topping.lower() == 'yes':
                    user_topping_selection = input("Enter the name of the topping you want to add: ")
                    if user_topping_selection.lower() == 'cheese':
                        cheese_topping = CheeseTopping()
                        pizzeria.create_pizza(pepperoni_pizza, [cheese_topping])
                    elif user_topping_selection.lower() == 'vegetable':
                        vegetable_topping = VegetableTopping()
                        pizzeria.create_pizza(pepperoni_pizza, [vegetable_topping])
                    elif user_topping_selection.lower() == 'chile':
                        chile_topping = ChileTopping()
                        pizzeria.create_pizza(pepperoni_pizza, [chile_topping])
                    elif user_topping_selection.lower() == 'pineapple':
                        pineapple_topping = CheeseTopping()
                        pizzeria.create_pizza(pepperoni_pizza, [pineapple_topping])
                    elif user_topping_selection.lower() == 'sweet bow':
                        sweetbow_topping = SweetBowTopping()
                        pizzeria.create_pizza(pepperoni_pizza, [sweetbow_topping])
                    else:
                        print("We don't have this topping")
                else:
                    print("Wrong answer")
            elif user_pizza_selection.lower() == 'hawaiian':
                hawaiian_pizza = HawaiianPizza()
                offer_topping = input("The same we have 5 toppings: 'Cheese', 'Vegetable', 'Chile', 'Pineapple', "
                                      "'Sweet bow'\n"
                                      "Do you want to add topping? (Yes/No): ")
                if offer_topping.lower() == 'no':
                    pizzeria.create_pizza(hawaiian_pizza)
                elif offer_topping.lower() == 'yes':
                    user_topping_selection = input("Enter the name of the topping you want to add: ")
                    if user_topping_selection.lower() == 'cheese':
                        cheese_topping = CheeseTopping()
                        pizzeria.create_pizza(hawaiian_pizza, [cheese_topping])
                    elif user_topping_selection.lower() == 'vegetable':
                        vegetable_topping = VegetableTopping()
                        pizzeria.create_pizza(hawaiian_pizza, [vegetable_topping])
                    elif user_topping_selection.lower() == 'chile':
                        chile_topping = ChileTopping()
                        pizzeria.create_pizza(hawaiian_pizza, [chile_topping])
                    elif user_topping_selection.lower() == 'pineapple':
                        pineapple_topping = CheeseTopping()
                        pizzeria.create_pizza(hawaiian_pizza, [pineapple_topping])
                    elif user_topping_selection.lower() == 'sweet bow':
                        sweetbow_topping = SweetBowTopping()
                        pizzeria.create_pizza(hawaiian_pizza, [sweetbow_topping])
                    else:
                        print("We don't have this topping")
                else:
                    print("Wrong answer")
            elif user_pizza_selection.lower() == 'fourcheese':
                fourcheese_pizza = FourCheesePizza()
                offer_topping = input("The same we have 5 toppings: 'Cheese', 'Vegetable', 'Chile', 'Pineapple', "
                                      "'Sweet bow'\n"
                                      "Do you want to add topping? (Yes/No): ")
                if offer_topping.lower() == 'no':
                    pizzeria.create_pizza(fourcheese_pizza)
                elif offer_topping.lower() == 'yes':
                    user_topping_selection = input("Enter the name of the topping you want to add: ")
                    if user_topping_selection.lower() == 'cheese':
                        cheese_topping = CheeseTopping()
                        pizzeria.create_pizza(fourcheese_pizza, [cheese_topping])
                    elif user_topping_selection.lower() == 'vegetable':
                        vegetable_topping = VegetableTopping()
                        pizzeria.create_pizza(fourcheese_pizza, [vegetable_topping])
                    elif user_topping_selection.lower() == 'chile':
                        chile_topping = ChileTopping()
                        pizzeria.create_pizza(fourcheese_pizza, [chile_topping])
                    elif user_topping_selection.lower() == 'pineapple':
                        pineapple_topping = CheeseTopping()
                        pizzeria.create_pizza(fourcheese_pizza, [pineapple_topping])
                    elif user_topping_selection.lower() == 'sweet bow':
                        sweetbow_topping = SweetBowTopping()
                        pizzeria.create_pizza(fourcheese_pizza, [sweetbow_topping])
                    else:
                        print("We don't have this topping")
                else:
                    print("Wrong answer")
            elif user_pizza_selection.lower() == 'veggie':
                veggie_pizza = VeggiePizza()
                offer_topping = input("The same we have 5 toppings: 'Cheese', 'Vegetable', 'Chile', 'Pineapple', "
                                      "'Sweet bow'\n"
                                      "Do you want to add topping? (Yes/No): ")
                if offer_topping.lower() == 'no':
                    pizzeria.create_pizza(veggie_pizza)
                elif offer_topping.lower() == 'yes':
                    user_topping_selection = input("Enter the name of the topping you want to add: ")
                    if user_topping_selection.lower() == 'cheese':
                        cheese_topping = CheeseTopping()
                        pizzeria.create_pizza(veggie_pizza, [cheese_topping])
                    elif user_topping_selection.lower() == 'vegetable':
                        vegetable_topping = VegetableTopping()
                        pizzeria.create_pizza(veggie_pizza, [vegetable_topping])
                    elif user_topping_selection.lower() == 'chile':
                        chile_topping = ChileTopping()
                        pizzeria.create_pizza(veggie_pizza, [chile_topping])
                    elif user_topping_selection.lower() == 'pineapple':
                        pineapple_topping = CheeseTopping()
                        pizzeria.create_pizza(veggie_pizza, [pineapple_topping])
                    elif user_topping_selection.lower() == 'sweet bow':
                        sweetbow_topping = SweetBowTopping()
                        pizzeria.create_pizza(veggie_pizza, [sweetbow_topping])
                    else:
                        print("We don't have this topping")
                else:
                    print("Wrong answer")
            else:
                print("We don't have this pizza :('")
        elif user_order.lower() =='exit':
            break
        elif user_order.lower() == 'dc':
            input_password = input('Input password for logging in develop console: ')
            if input_password == password:
                develope_commands = input("Commands:\n"
                                          "1. Calculate income,\n"
                                          "2. Calculate expenses\n"
                                          "3. Calculate_revenue\n"
                                          "4. Exit.\n"
                                          "Enter number of command: ")
                if develope_commands == '1':
                    print(pizzeria.calculate_income())
                elif develope_commands == '2':
                    print(pizzeria.calculate_expenses())
                elif develope_commands == '3':
                    print(pizzeria.calculate_revenue())
                elif develope_commands == '4':
                    break
                else:
                    print("Wrong command")
            else:
                print("Wrong password")
                break
        else:
            print("Wrong command :(")


main_pizzeria()
# Очень крутое задание, пришлось немло так посидеть ))
