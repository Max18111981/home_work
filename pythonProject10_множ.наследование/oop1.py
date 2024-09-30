# Создать базовый класс Фигура с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади.


class Figure:
    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError('Подклассы должны реализовывать метод calculate_area')


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class RightTriangle(Figure):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        super().__init__()
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height


rectangle = Rectangle(4, 5)
print(rectangle.calculate_area())

circle = Circle(3)
print(circle.calculate_area())

triangle = RightTriangle(3, 4)
print(triangle.calculate_area())

trapezoid = Trapezoid(3, 5, 4)
print(trapezoid.calculate_area())

