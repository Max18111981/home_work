# Создайте класс Car, который содержит информацию о марке автомобиля,
# максимальной скорости и текущей скорости.
# Инкапсулируйте переменные с текущей скоростью, чтобы нельзя было напрямую её изменять.
#
# Условия:
#
#  • Создайте конструктор, принимающий марку и максимальную скорость.
#  • Создайте методы для увеличения и уменьшения скорости, контролируя,
# чтобы скорость не превышала максимальную.
#  • Добавьте метод для отображения текущей скорости.


class Car:
    def __init__(self, brand, max_speed):
        self.__brand = brand
        self.__max_speed = max_speed
        self.__current_speed = 0

    def accelerate(self, speed):
        if self.__current_speed + speed <= self.__max_speed:
            self.__current_speed += speed
        else:
            self.__current_speed = self.__max_speed

    def brake(self, speed):
        if self.__current_speed - speed >= 0:
            self.__current_speed -= speed
        else:
            self.__current_speed = 0

    def display_current_speed(self):
        print(f'Текущая скорость: {self.__current_speed} km/h')

    def __str__(self):
        return f'Бренд: {self.__brand}, Максимальная скорость: {self.__max_speed} km/h, Текущая скорость: {self.__current_speed} km/h'


my_car = Car("Toyota", 200)
print(my_car)

my_car.accelerate(90)
print(my_car)

my_car.brake(20)
print(my_car)