# Создайте базовый класс Shape для рисования плоских фигур. Определите методы: Show() — вывод на экран информации
# о фигуре; Save() — сохранение фигуры в файл; Load() — считывание фигуры из файла.
# Определите производные классы: Square — квадрат, который характеризуется координатами левого верхнего угла и длиной
# стороны; Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами; Circle — окружность с
# заданными координатами центра и радиусом; Ellipse — эллипс с заданными координатами верхнего угла описанного вокруг
# него прямоугольника со сторонами, параллельными осям координат, и размерами этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл, загрузите в другой список и отобразите информацию о каждой из фигур


class Shape:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def Show(self):
        print(f"Position: ({self._x}, {self._y})")

    def Save(self, filename):
        with open(file=filename, mode="w", encoding="utf-8") as file:
            file.write(f"{self._x},{self._y}")

    def Load(self, filename):
        with open(file=filename, mode="r", encoding="utf-8") as file:
            data = file.read().split(",")
            self._x = int(data[0])
            self._y = int(data[1])


class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__(x, y)
        self._side_length = side_length

    def Show(self):
        super().Show()
        print(f"Shape: Square\nSide length: {self._side_length}")

    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, value):
        self._side_length = value


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self._width = width
        self._height = height

    def Show(self):
        super().Show()
        print(f"Shape: Rectangle\nWidth: {self._width}\nHeight: {self._height}")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self._radius = radius

    def Show(self):
        super().Show()
        print(f"Shape: Circle\nRadius: {self._radius}")

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self._width = width
        self._height = height

    def Show(self):
        super().Show()
        print(f"Shape: Ellipse\nWidth: {self._width}\nHeight: {self._height}")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


shapes = [
    Square(5, 5, 15),
    Rectangle(7, 7, 20, 15),
    Circle(10, 10, 5),
    Ellipse(30, 30, 30, 20)
]

for i, shape in enumerate(shapes):
    shape.Save(f"shape_{i}.txt")

new_shapes = []
for i in range(len(shapes)):
    if isinstance(shapes[i], Square):
        shape = Square(10, 10, 30)
    elif isinstance(shapes[i], Rectangle):
        shape = Rectangle(7, 7, 20, 15)
    elif isinstance(shapes[i], Circle):
        shape = Circle(10, 10, 5)
    elif isinstance(shapes[i], Ellipse):
        shape = Ellipse(30, 30, 30, 20)
    else:
        raise ValueError("Invalid shape")

    shape.Load(f"shape_{i}.txt")
    new_shapes.append(shape)

for shape in new_shapes:
    shape.Show()
    print("-----------")