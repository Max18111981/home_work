

# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о классе)
# класс Blender (содержит информацию о блендере),
# класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.


class Device:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer

    @staticmethod
    def get_device_info(device):
        return f'Устройство: {device.name}, Производитель: {device.manufacturer}'


class CoffeeMachine(Device):
    def __init__(self, name, manufacturer, coffee_capacity):
        super().__init__(name, manufacturer)
        self.coffee_capacity = coffee_capacity

    def make_coffee(self):
        return f'Кофе готов! Объем кофе: {self.coffee_capacity} мл'


class Blender(Device):
    def __init__(self, name, manufacturer, speed):
        super().__init__(name, manufacturer)
        self.speed = speed

    def blend(self):
        return f'Блендер работает на скорости {self.speed} оборотов в минуту'


class MeatGrinder(Device):
    def __init__(self, name, manufacturer, grinding_capacity):
        super().__init__(name, manufacturer)
        self.grinding_capacity = grinding_capacity

    def grind(self):
        return f'Мясорубка измельчает мясо с мощностью {self.grinding_capacity} кг/час'
    

coffee_machine = CoffeeMachine("Кофемашина", "Bosch", 200)
print(Device.get_device_info(coffee_machine))
print(coffee_machine.make_coffee())

blender = Blender("Блендер", "Philips", 500)
print(Device.get_device_info(blender))
print(blender.blend())

meat_grinder = MeatGrinder("Мясорубка", "Moulinex", 1.5)
print(Device.get_device_info(meat_grinder))
print(meat_grinder.grind())