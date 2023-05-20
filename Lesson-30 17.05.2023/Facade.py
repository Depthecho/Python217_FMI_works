# Представьте, что у вас есть система со
# значительным количеством объектов. Каждый
# объект предлагает богатый набор методов API.
# С этой системой можно делать много чего, но
# как насчет упрощения интерфейса? Почему бы
# не добавить объект интерфейса, предоставляющий
# хорошо продуманное подмножество всех методов API?
# Фасад!

# Подсистема 1
class Washing:
    def wash(self):
        print("Washing...")

# Подсистема 2
class Rinsing:
    def rinse(self):
        print("Rinsing...")

# Подсистема 3
class Spinning:
    def spin(self):
        print("Spinning...")

# Фасад, предоставляющий доступ к действиям подсистем
class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def startWashing(self):
        self.washing.wash()
        self.startRinsing()

    def startRinsing(self):
        self.rinsing.rinse()
        self.spinning.spin()


washingMachine = WashingMachine()
washingMachine.startWashing()
