import csv

students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is in {student['home']}")


# def get_name(student):
#     return student["name"]


# def get_home(student):
#     return student["home"]

# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['home']}")
