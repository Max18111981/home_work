# Создайте базовый класс Shape для рисования плоских
# фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# 1
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами
# этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл,
# загрузите в другой список и отобразите информацию о
# каждой из фигур.


import json


class Shape:
    def __init__(self):
        pass

    def show(self):
        raise NotImplementedError("Subclasses must implement show method ")

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)

    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            if data['type'] == 'Square':
                return Square(data['x'], data['y'], data['side'])
            elif data['type'] == 'Rectangle':
                return Rectangle(data['x'], data['y'], data['width'], data['height'])
            elif data['type'] == 'Circle':
                return Circle(data['x'], data['y'], data['radius'])
            elif data['type'] == 'Ellipse':
                return Ellipse(data['x'], data['y'], data['width'], data['height'])
            else:
                raise ValueError("Invalid shape type")


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__()
        self.type = 'Square'
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        return f"Square at ({self.x}, {self.y}) with side {self.side}"


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.type = 'Rectangle'
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        return f"Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}"


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.type = 'Circle'
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        return f"Circle at ({self.x}, {self.y}) with radius {self.radius}"


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.type = 'Ellipse'
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        return f"Ellipse at ({self.x}, {self.y}) with width {self.width} and height {self.height}"


# Create a list of shapes
shapes = [
    Square(1, 2, 3),
    Rectangle(4, 5, 6, 7),
    Circle(8, 9, 10),
    Ellipse(11, 12, 13, 14)
]

# Save the shapes to a file
for i, shape in enumerate(shapes):
    shape.save(f"shape_{i}.json")

# Load the shapes from the file
loaded_shapes = []
for i in range(len(shapes)):
    loaded_shapes.append(Shape.load(f"shape_{i}.json"))

# Show the information about each shape
for shape in loaded_shapes:
    print(shape.show())
    