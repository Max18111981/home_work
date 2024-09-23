# К уже реализованному классу «Дробь» добавьте статический метод,
# который при вызове возвращает количество созданных объектов класса «Дробь».

class Fraction:
    instances_created = 0

    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        Fraction.instances_created += 1

    @staticmethod
    def get_instances_created():
        return Fraction.instances_created

f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
f3 = Fraction(5, 6)

print(Fraction.get_instances_created())