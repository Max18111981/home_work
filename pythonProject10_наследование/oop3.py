# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) и
# поле для хранения копеек (центы, евроценты, копейки
# и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.


class Money:
    def __init__(self, whole_part, fractional_part, currency):
        self.whole_part = whole_part
        self.fractional_part = fractional_part
        self.currency = currency

    @staticmethod
    def format_money(money):
        return f'{money.whole_part} {money.currency} {money.fractional_part} {Money.get_fractional_unit(money.currency)}'

    @staticmethod
    def get_fractional_unit(currency):
        if currency == 'USD':
            return 'cents'
        elif currency == 'EUR':
            return 'eurocents'
        elif currency == "UAH":
            return 'kopiyok'
        else:
            return 'unknown'

    def set_whole_part(self, whole_part):
        self.whole_part = whole_part

    def set_fractional_part(self, fractional_part):
        self.fractional_part = fractional_part

    def __str__(self):
        return Money.format_money(self)


money = Money(10, 50, 'USD')
print(money)

money.set_whole_part(20)
print(money)

money.set_fractional_part(75)
print(money)


