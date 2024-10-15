# Создайте класс ComplexNumber,
# который будет представлять комплексное число и реализуйте сложение и вычитание комплексных чисел,
# используя магические методы add() и sub().
# Условия:
#  • Конструктор должен принимать действительную и мнимую части.
#  • Реализуйте магические методы для сложения и вычитания.


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f'{self.real}{sign}{abs(self.imag)}i'
