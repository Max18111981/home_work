# Создайте абстрактный класс Shape, который имеет абстрактный метод get_area().
# Затем создайте классы Square и Triangle,
# которые наследуются от этого абстрактного класса и реализуют свои версии метода get_area().
#
# Условия:
#
#  • Класс Square должен принимать длину стороны, а класс Triangle — основание и высоту.
#  • Метод get_area() должен возвращать площадь фигуры.


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * (self.base * self.height)
    