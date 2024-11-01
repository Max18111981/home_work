import pandas as pd


class Stadium:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'capacity': self.capacity
        }


if __name__ == "__main__":
    stadiums = [
        Stadium("Wembley Stadium", "London, UK", 90000),
        Stadium("Camp Nou", "Barcelona, Spain", 99354),
        Stadium("Old Trafford", "Manchester, UK", 74879)
    ]

    df = pd.DataFrame([stadium.to_dict() for stadium in stadiums])
    print(df)
    df.to_csv('stadiums.csv', index=False)