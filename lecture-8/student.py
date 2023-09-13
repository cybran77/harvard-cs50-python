class Student:
    def __init__(self, name, house=None):
        if not name:
            raise ValueError("Name is required")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("House is invalid")
        self.name = name
        self.house = house

    # def get_name(self):
    #     return self.name

    # def get_house(self):
    #     return self.house


def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(f"{student.name} from {student.house}")


def get_student():    
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
