# К уже реализованному классу «Книга»
# добавьте возможность упаковки и распаковки данных
# с использованием json и pickle.


import json
import pickle


class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def to_json(self):
        data = {
            'title': self.__title,
            'author': self.__author,
            'year': self.__year
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data['title'], data['author'], data['year'])

    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)


if __name__ == "__main__":
    book = Book("1984", "George Orwell", 1949)

    json_data = book.to_json()
    print("JSON:", json_data)

    new_book_from_json = Book.from_json(json_data)
    print("Из JSON:", new_book_from_json.get_title(), new_book_from_json.get_author(), new_book_from_json.get_year())

    pickle_data = book.to_pickle()
    print("Pickle:", pickle_data)

    new_book_from_pickle = Book.from_pickle(pickle_data)
    print("Из Pickle:", new_book_from_pickle.get_title(), new_book_from_pickle.get_author(), new_book_from_pickle.get_year())