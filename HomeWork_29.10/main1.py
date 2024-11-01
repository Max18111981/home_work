# К уже реализованному классу «Автомобиль» добавьте
# возможность упаковки и распаковки данных с использованием json и pickle.


import json
import pickle


class Automobile:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def to_json(self):
        data = {
            'make': self.__make,
            'model': self.__model,
            'year': self.__year
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data['make'], data['model'], data['year'])

    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)


if __name__ == "__main__":
    car = Automobile("Toyota", "Camry", 2023)

    json_data = car.to_json()
    print("JSON:", json_data)

    new_car_from_json = Automobile.from_json(json_data)
    print("Из JSON:", new_car_from_json.get_make(), new_car_from_json.get_model(), new_car_from_json.get_year())

    pickle_data = car.to_pickle()
    print("Pickle:", pickle_data)

    new_car_from_pickle = Automobile.from_pickle(pickle_data)
    print("Из Pickle:", new_car_from_pickle.get_make(), new_car_from_pickle.get_model(), new_car_from_pickle.get_year())