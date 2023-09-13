class Student:
    def __init__(self, name, house=None, patronus=None):
        if not name:
            raise ValueError("Name is required")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("House is invalid")
        self.name = name
        self.house = house
        self.patronus = patronus.lower() if patronus else None

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "stag":
                return "🦌"
            case "otter":
                return "🦦"
            case "jack russell terrier":
                return "🐶"
            case _:
                return "🐱"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
