# Есть некоторый словарь, который хранит названия
# музыкальных групп(исполнителей) и альбомов.
# Название группы используется в качестве (ключа, название)
# альбомов в качестве значения. Необходимо реализовать:
# добавление данных, удаление данных, поиск данных,
# редактирование данных, сохранение и загрузку данных
# (используя упаковку и распаковку).


import  pickle


import pickle


class MusicManager:
    def __init__(self):
        self.data = {}

    def add_group(self, group, album):
        if group in self.data:
            self.data[group].append(album)
            print(f'Альбом {album} добавлен к группе {group}.')
        else:
            self.data[group] = [album]
            print(f'Группа {group} с альбомом {album} добавлена.')

    def remove_group(self, group):
        if group in self.data:
            del self.data[group]
            print(f'Группа {group} удалена.')
        else:
            print(f'Группа {group} не найдена.')

    def remove_album(self, group, album):
        if group in self.data:
            if album in self.data[group]:
                self.data[group].remove(album)
                print(f'Альбом {album} удален из группы {group}.')
            else:
                print(f'Альбом {album} не найден в группе {group}.')
        else:
            print(f'Группа {group} не найдена.')

    def find_group(self, group):
        albums = self.data.get(group)
        if albums:
            print(f'Альбомы группы {group}: {', '.join(albums)}')
        else:
            print(f'Группа {group} не найдена.')

    def edit_group(self, old_group, new_group):
        if old_group in self.data:
            self.data[new_group] = self.data.pop(old_group)
            print(f'Группа {old_group} переименована в {new_group}.')
        else:
            print(f'Группа {old_group} не найдена.')

    def edit_album(self, group, old_album, new_album):
        if group in self.data:
            if old_album in self.data[group]:
                self.data[group][self.data[group].index(old_album)] = new_album
                print(f'Альбом {old_album} группы {group} переименован в {new_album}.')
            else:
                print(f"Альбом '{old_album}' не найден в группе '{group}'.")
        else:
            print(f'Группа {group} не найдена.')

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


manager = MusicManager()
manager.add_group("The Beatles", "Sgt. Pepper's Lonely Hearts Club Band")
manager.add_group("The Beatles", "Abbey Road")
manager.add_group("Queen", "A Night at the Opera")
manager.find_group("The Beatles")
manager.edit_album("The Beatles", "Sgt. Pepper's Lonely Hearts Club Band", "Sgt. Pepper's")
manager.remove_album("The Beatles", "Abbey Road")
manager.save_data("music.pkl")
manager.load_data("music.pkl")
