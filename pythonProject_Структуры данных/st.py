# Пользователь вводит с клавиатуры набор чисел. Полученные числа необходимо сохранить в список (тип
# списка нужно выбрать в зависимости от поставленной
# ниже задачи). После чего нужно показать меню, в котором
# предложить пользователю набор пунктов:
# 1. Добавить новое число в список (если такое число существует в списке, нужно вывести сообщение пользователю об этом, без добавления числа).
# 2. Удалить все вхождения числа из списка (пользователь
# вводит с клавиатуры число для удаления).
# 3. Показать содержимое списка (в зависимости от выбора пользователя список нужно показать с начала
# или с конца).
# 4. Проверить есть ли значение в списке.
# 5. Заменить значение в списке (пользователь определяет заменить ли только первое вхождение или все
# вхождения).
# В зависимости от выбора пользователя выполняется
# действие, после чего меню отображается снова


numbers = []

while True:

    user_input = input("Enter a set of numbers (separated by spaces): ")
    numbers = [int(x) for x in user_input.split()]


    print("\nMenu:")
    print("1. Add a new number to the list")
    print("2. Remove all occurrences of a number from the list")
    print("3. Show the contents of the list")
    print("4. Check if a value is in the list")
    print("5. Replace a value in the list")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_number = int(input("Enter a new number: "))
        if new_number in numbers:
            print("Number already exists in the list!")
        else:
            numbers.append(new_number)

    elif choice == 2:
        remove_number = int(input("Enter a number to remove: "))
        numbers = [x for x in numbers if x != remove_number]

    elif choice == 3:
        show_from_beginning = input("Show from beginning? (y/n): ")
        if show_from_beginning.lower() == 'y':
            print(numbers)
        else:
            print(numbers[::-1])

    elif choice == 4:
        check_number = int(input("Enter a number to check: "))
        if check_number in numbers:
            print("Number is in the list!")
        else:
            print("Number is not in the list!")

    elif choice == 5:
        replace_number = int(input("Enter a number to replace: "))
        replace_with = int(input("Enter a new value: "))
        replace_all = input("Replace all occurrences? (y/n): ")
        if replace_all.lower() == 'y':
            numbers = [replace_with if x == replace_number else x for x in numbers]
        else:
            if replace_number in numbers:
                numbers[numbers.index(replace_number)] = replace_with

    elif choice == 6:
        break

    else:
        print("Invalid choice. Please try again!")