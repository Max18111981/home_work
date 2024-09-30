# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
# информацию о фигуре)


class Figure:
    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError('Подклассы должны реализовывать метод calculate_area')

    def __int__(self):
        raise NotImplementedError('Подклассы должны реализовывать метод __int__')

    def __str__(self):
        raise NotImplementedError('Подклассы должны реализовывать метод __str__')


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def __int__(self):
        return self.calculate_area()

    def __str__(self):
        return f'Прямоугольник длиной {self.length} и шириной {self.width}'


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def __float__(self):
        return self.calculate_area()

    def __str__(self):
        return f'Окружность с радиусом {self.radius}'


class RightTriangle(Figure):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def __float__(self):
        return self.calculate_area()

    def __str__(self):
        return f'Прямоугольный треугольник с основанием {self.base} и высотой {self.height}'


class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        super().__init__()
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __float__(self):
        return self.calculate_area()

    def __str__(self):
        return f'Трапеция с основанием1 {self.base1}, основанием2 {self.base2} и высотой {self.height}'


rectangle = Rectangle(4, 5)
print(int(rectangle))
print(str(rectangle))

circle = Circle(3)
print(float(circle))
print(str(circle))

triangle = RightTriangle(3, 4)
print(float(triangle))
print(str(triangle))

trapezoid = Trapezoid(3, 5, 4)
print(float(trapezoid))
print(str(trapezoid))