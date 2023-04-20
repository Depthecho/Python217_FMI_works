# Создайте класс Device,который содержит информацию об устройстве. С помощью механизма наследования,реализуйте
# класс класс CoffeeMachine (содержит информацию о кофемашине), Blender(содержитинформациюоблендере),
# класс MeatGrinder (содержит информацию о мясорубке).Каждый из классов должен содержать необходимые для работы методы

class Device:
    def __init__(self, name, brand, model):
        self.name = name
        self.brand = brand
        self.model = model

    def get_info(self):
        return f"{self.brand} {self.model} {self.name}"


class CoffeeMachine(Device):
    def __init__(self, name, brand, model, coffee_type):
        Device.__init__(self, name, brand, model)
        self.coffee_type = coffee_type

    def get_info_coffee(self):
        return f"Эта коффемашина делает коффе: {self.coffee_type}"


class Blender(Device):
    def __init__(self, name, brand, model, power):
        Device.__init__(self, name, brand, model)
        self.power = power

    def get_info_blend(self):
        return f"Блендер имеет мощность {self.power} ватт"


class MeatGrinder(Device):
    def __init__(self, name, brand, model, material):
        Device.__init__(self, name, brand, model)
        self.material = material

    def get_info_grind_meat(self):
        return f"Мясорубка измельчает еду с помощью {self.material} лезвий"

coffee_machine = CoffeeMachine("1", "2", "3", "4")
print(coffee_machine.get_info())  # Breville BES870XL Coffee Machine
print(coffee_machine.get_info_coffee())  # Making espresso coffee

blender = Blender("1", "2", "3", 4)
print(blender.get_info())
print(blender.get_info_blend())

meat_grinder = MeatGrinder("1", "2", "3", "4")
print(meat_grinder.get_info())
print(meat_grinder.get_info_grind_meat())