# Factory Method
import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

# Шаблон проектирования Factory Method поможет нам
# абстрагировать доступные фигуры от клиента, т. е.
# клиенту не нужно знать все доступные фигуры, а
# нужно только создавать то, что ему нужно во
# время выполнения. Это также позволит нам
# централизовать и инкапсулировать создание объекта.


class ShapeFactory:

    @staticmethod
    def create_shape(name):
        if name == 'circle':
            radius = input("Enter the radius of the circle: ")
            return Circle(float(radius))

        elif name == 'rectangle':
            height = input("Enter the height of the rectangle: ")
            width = input("Enter the width of the rectangle: ")
            return Rectangle(int(height), int(width))

        elif name == 'square':
            width = input("Enter the width of the square: ")
            return Square(int(width))
        else:
            raise ValueError('You cannot create this shape!')


factory = ShapeFactory()
shapes = []
for i in range(3):
    shape = input('Input name of shape to create: ')
    shapes.append(factory.create_shape(shape))
    print(shapes[-1])
    print(shapes[-1].calculate_area(), shapes[-1].calculate_perimeter())

