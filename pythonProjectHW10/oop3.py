# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

class UnitConverter:
    conversions_made = 0

    @staticmethod
    def meter_to_foot(meter):
        UnitConverter.conversions_made += 1
        return meter * 3.28084

    @staticmethod
    def foot_to_meter(foot):
        UnitConverter.conversions_made += 1
        return foot / 3.28084

    @staticmethod
    def kilogram_to_pound(kilogram):
        UnitConverter.conversions_made += 1
        return kilogram * 2.20462

    @staticmethod
    def pound_to_kilogram(pound):
        UnitConverter.conversions_made += 1
        return pound / 2.20462

    @staticmethod
    def liter_to_gallon(liter):
        UnitConverter.conversions_made += 1
        return liter * 0.264172

    @staticmethod
    def gallon_to_liter(gallon):
        UnitConverter.conversions_made += 1
        return gallon / 0.264172

    @staticmethod
    def get_conversions_made():
        return UnitConverter.conversions_made
