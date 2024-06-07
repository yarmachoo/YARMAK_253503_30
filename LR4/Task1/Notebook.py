import pickle
import datetime
import csv
class Notebook():
    def __init__(self):
        """Initializer of class"""
        self.friends = []

    def add_note(self, friend):
        """Add new element to list (friends)"""
        self.friends.append(friend)

    def del_note(self, friend):
        """Delete the element of list (friends)"""
        self.friends.remove(friend)

    def print_friends_by_age(self, age):
        """Print elements of list (friends)"""
        for friend in self.friends:
            if friend.birth_year + age == datetime.date.today().year:
                print(friend)

    def serialize_to_file(self, file_name):
        """Serialize list (friends)"""
        with open(file_name, 'wb') as file:
            pickle.dump(self.friends, file)

    @staticmethod
    def deserialize_from_file(file_name):
        """Deserialize file to list (friends)"""
        notebook = Notebook()
        with open(file_name, 'rb') as file:
            notebook.friends = pickle.load(file)
        return notebook

    def serialize_to_file_csv(self, file_name):
        with open(file_name, 'w', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "day", "month", "year"], quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for friend in self.friends:
                writer.writerow(dict(name=friend.name, day=friend.birth_date, month=friend.birth_month, year=friend.birth_year))

    @staticmethod
    def deserialize_from_file_csv(file_name):
        rows = []
        with open(file_name, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

        for row in rows:
            print(row)
