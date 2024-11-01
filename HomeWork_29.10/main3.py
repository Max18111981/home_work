# К уже реализованному классу «Стадион» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.


import json
import pickle


class Stadium:
    def __init__(self, name, location, capacity):
        self.__name = name
        self.__location = location
        self.__capacity = capacity

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_capacity(self):
        return self.__capacity

    def to_json(self):
        data = {
            'name': self.__name,
            'location': self.__location,
            'capacity': self.__capacity
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data['name'], data['location'], data['capacity'])

    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)


if __name__ == "__main__":
    stadium = Stadium("Wembley Stadium", "London, UK", 90000)

    json_data = stadium.to_json()
    print("JSON:", json_data)

    new_stadium_from_json = Stadium.from_json(json_data)
    print("Из JSON:", new_stadium_from_json.get_name(), new_stadium_from_json.get_location(), new_stadium_from_json.get_capacity())

    pickle_data = stadium.to_pickle()
    print("Pickle:", pickle_data)

    new_stadium_from_pickle = Stadium.from_pickle(pickle_data)
    print("Из Pickle:", new_stadium_from_pickle.get_name(), new_stadium_from_pickle.get_location(), new_stadium_from_pickle.get_capacity())