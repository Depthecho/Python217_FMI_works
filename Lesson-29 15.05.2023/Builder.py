# Builder Method — это порождающий шаблон проектирования,
# целью которого является отделить построение сложного
# объекта от его представления, чтобы один и тот же
# процесс построения мог создавать разные представления.

class Robot:
    def __init__(self):
        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []

    def __str__(self):
        string = ""
        if self.bipedal:
            string += "BIPEDAL "
        if self.quadripedal:
            string += "QUADRIPEDAL "
        if self.flying:
            string += "FLYING ROBOT "
        if self.wheeled:
            string += "ROBOT ON WHEELS\n"
        else:
            string += "ROBOT\n"
        if self.traversal:
            string += "Traversal modules installed:\n"
        for module in self.traversal:
            string += "- " + str(module) + "\n"
        if self.detection_systems:
            string += "Detection systems installed:\n"
        for system in self.detection_systems:
            string += "- " + str(system) + "\n"
        return string


class BipedalLegs:
    def __str__(self):
        return "two legs"


class QuadripedalLegs:
    def __str__(self):
        return "four legs"


class Arms:
    def __str__(self):
        return "arms"


class Wings:
    def __str__(self):
        return "wings"


class Blades:
    def __str__(self):
        return "blades"


class FourWheels:
    def __str__(self):
        return "four wheels"


class TwoWheels:
    def __str__(self):
        return "two wheels"


class CameraDetectionSystem:
    def __str__(self):
        return "cameras"


class InfraredDetectionSystem:
    def __str__(self):
        return "infrared"


from abc import ABC, abstractmethod


class RobotBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_traversal(self):
        pass

    @abstractmethod
    def build_detection_system(self):
        pass


class AndroidBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.bipedal = True
        self.product.traversal.append(BipedalLegs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        self.product.detection_systems.append(CameraDetectionSystem())


class AutonomousCarBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.wheeled = True
        self.product.traversal.append(FourWheels())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())


# builder = AndroidBuilder()
# builder.build_traversal()
# builder.build_detection_system()
# print(builder.get_product())
#
#
# builder = AutonomousCarBuilder()
# builder.build_traversal()
# builder.build_detection_system()
# print(builder.get_product())


# Если в полях нашего продукта используются
# относительно стандартные конструкторы, мы
# можем даже создать так называемого директора
# для управления конкретными сборщиками:

class Director:

    def make_android(self, builder=AndroidBuilder()):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_autonomous_car(self, builder=AutonomousCarBuilder()):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()


director = Director()
builder = AndroidBuilder()
print(director.make_android(builder))

# Тем не менее, шаблон Builder не имеет большого
# смысла для небольших, простых классов, поскольку
# добавленная логика для их построения просто
# добавляет сложности.
