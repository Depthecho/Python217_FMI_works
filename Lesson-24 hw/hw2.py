# Создайте класс Ship(который содержити нформацию о корабле).С помощью механизма наследования, реализуйте класс Frigate
# (содержит информацию о фрегате),класс Destroyer(содержит информацию об эсминце),класс Cruiser
# (содержит информацию о крейсере).Каждый из классов должен содержать необходимые для работы методы

class Ship:
    def __init__(self, name, length, location):
        self.name = name
        self.length = length
        self.location = location

    def get_info(self):
        return f"Корабль: {self.name}, длина: {self.length}, локация: {self.location}"


class Frigate(Ship):
    def __init__(self, name, length, location, mission):
        Ship.__init__(self, name, length, location)
        self.mission = mission

    def frigate_mission(self):
        return f"Фригат {self.name} выехал с очередной миссией: {self.mission}"


class Destroyer(Ship):
    def __init__(self, name, length, location, target):
        Ship.__init__(self, name, length, location)
        self.target = target

    def destroyers_target(self):
        return f"Эсминец скоро нчнёт огонь по {self.target}"


class Cruiser(Ship):
    def __init__(self, name, length, location, num_ppl):
        Ship.__init__(self, name, length, location)
        self.num_ppl = num_ppl

    def ppl_on_cruiser(self):
        return f"На крейсере находится {self.num_ppl} людей"

frigate = Frigate("1", 2, "3", 4)
print(frigate.get_info())  # USS Constitution, length: 204, displacement: 2200
print(frigate.frigate_mission())  # Frigate USS Constitution is firing 30 guns

destroyer = Destroyer("1", 2, "3", 4)
print(destroyer.get_info())
print(destroyer.destroyers_target())

cruiser = Cruiser("1", 2, "3", 4)
print(cruiser.get_info())
print(cruiser.ppl_on_cruiser())