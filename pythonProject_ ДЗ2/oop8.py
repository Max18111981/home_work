# Есть некоторый словарь, который хранит названия
# стран и столиц. Название страны используется в качестве
# ключа, название столицыв качестве значения. Необходимо
# реализовать: добавление данных, удаление данных, поиск
# данных, редактирование данных, сохранение и загрузку
# данных (используя упаковку и распаковку).


import pickle


class CountryCapitalManager:
    def __init__(self):
        self.data = {}

    def add_country(self, country, capital):
        self.data[country] = capital
        print(f'Страна {country} с столицей {capital} добавлена.')

    def remove_country(self, country):
        if country in self.data:
            del self.data[country]
            print(f'Страна {country} удалена.')
        else:
            print(f'Страна {country} не найдена.')

    def find_country(self, country):
        capital = self.data.get(country)
        if capital:
            print(f'Столица страны {country}: {capital}')
        else:
            print(f'Страна {country} не найдена.')

    def edit_country(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
            print(f'Столица страны {country} изменена на {new_capital}.')
        else:
            print(f'Страна {country} не найдена.')

    def save_data(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.data, file)
            print('Данные сохранены.')

    def load_data(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
                print('Данные загружены.')
        except FileNotFoundError:
            print('Файл не найден.')


manager = CountryCapitalManager()
manager.add_country()
manager.add_country()
manager.find_country()
manager.edit_country()
manager.remove_country()
manager.save_data()
manager.load_data()