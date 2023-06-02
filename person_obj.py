import pickle

db = {}
db_path = "my_pickle_db.pickle"


def save_to_pickle(obj1, path):
    with open(path, "wb") as f:
        pickle.dump(obj1, f)


def read_from_pickle(db1, path):
    with open(path, "rb") as f:
        db1 = pickle.load(f)
    return db1


class person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address
        db[self.name] = self
        save_to_pickle(db, db_path)

    def __str__(self):
        return f"Name = {self.name}\tAge= {self.age}\tAddress= {self.address}"


db = read_from_pickle(db, db_path)


def get_input():
    objs = []
    while True:
        obj_name = input("Enter name (or 0 to finish): ")
        if obj_name == "0":
            return objs
        obj_age = input(f"Enter {obj_name}'s age: ")
        obj_addr = input(f"Enter {obj_name}'s address: ")
        objs.append(person(obj_name, int(obj_age), obj_addr))
        print()


get_input()
print()
for obj, value in db.items():
    print(value)


