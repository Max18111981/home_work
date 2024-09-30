# Создайте класс Ship, который содержит информацию
# о корабле.
# С помощью механизма наследования, реализуйте
# класс Frigate (содержит информацию о фрегате), класс
# Destroyer (содержит информацию об эсминце), класс
# Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые
# для работы методы.


class Ship:
    def __init__(self, name, manufacturer, displacement):
        self.name = name
        self.manufacturer = manufacturer
        self.displacement = displacement

    @staticmethod
    def get_ship_info(ship):
        return f'Корабль: {ship.name}, Производитель: {ship.manufacturer}, Водоизмещение: {ship.displacement} тонн'


class Frigate(Ship):
    def __init__(self, name, manufacturer, displacement, speed):
        super().__init__(name, manufacturer, displacement)
        self.speed = speed

    def patrol(self):
        return f'Фрегат {self.name} патрулирует на скорости {self.speed} узлов'


class Destroyer(Ship):
    def __init__(self, name, manufacturer, displacement, firepower):
        super().__init__(name, manufacturer, displacement)
        self.firepower = firepower

    def attack(self):
        return f'Эсминец {self.name} атакует с мощностью {self.firepower} единиц'


class Cruiser(Ship):
    def __init__(self, name, manufacturer, displacement, cruising):
        super().__init__(name, manufacturer, displacement)
        self.cruising = cruising

    def cruise(self):
        return f'Крейсер {self.name} крейсирует на расстоянии {self.cruising} морских миль'

    