class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Name is required")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


student = Student("Harry", "Gryffindor")
print(student.name, student.house)

professor = Professor("Snape", "Potions")
print(professor.name, professor.subject)
