# Реализуйте класс стека для работы со строками (стек
# строк).
# Стек должен иметь фиксированный размер.
# Реализуйте набор операций для работы со стеком:
# ■ помещение строки в стек;
# ■ выталкивание строки из стека;
# ■ подсчет количества строк в стеке;
# ■ проверку пустой ли стек;
# ■ проверку полный ли стек;
# ■ очистку стека;
# ■ получение значения без выталкивания верхней строки
# из стека.
# При старте приложения нужно отобразить меню с
# помощью, которого пользователь может выбрать необходимую операцию.
# Задание 3
# Измените стек из второго задания, таким образом,
# чтобы его размер был нефиксированным.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)

    def pop(self):
        if self.is_empty():
            return "Стек пуст"
        return self.stack.pop()

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return False  # Стек не имеет фиксированный размер

    def clear(self):
        self.stack = []

    def peek(self):
        if self.is_empty():
            return "Стек пуст"
        return self.stack[-1]


def main():
    stack = Stack()

    while True:
        print("\nМеню:")
        print("1. Поместить строку в стек")
        print("2. Вытолкнуть строку из стека")
        print("3. Подсчитать количество строк в стеке")
        print("4. Проверить пустой ли стек")
        print("5. Проверить полный ли стек")
        print("6. Очистить стек")
        print("7. Получить значение без выталкивания верхней строки из стека")
        print("8. Выход")

        choice = int(input("Введите ваш выбор: "))

        if choice == 1:
            string = input("Введите строку: ")
            stack.push(string)

        elif choice == 2:
            print(stack.pop())

        elif choice == 3:
            print("Количество строк в стеке:", stack.count())

        elif choice == 4:
            if stack.is_empty():
                print("Стек пуст")
            else:
                print("Стек не пуст")

        elif choice == 5:
            if stack.is_full():
                print("Стек полный")
            else:
                print("Стек не полный")

        elif choice == 6:
            stack.clear()
            print("Стек очищен")

        elif choice == 7:
            print(stack.peek())

        elif choice == 8:
            break

        else:
            print("Неправильный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()