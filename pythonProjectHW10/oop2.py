# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температурыи
# возвращать это значение с помощью статического метода.

class TemperatureConverter:
    conversions_made = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversions_made += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversions_made += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversions_made():
        return TemperatureConverter.conversions_made