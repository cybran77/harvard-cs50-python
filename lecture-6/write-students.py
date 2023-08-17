import csv

name = input("What is your name? ")
home = input("What is your home? ")

# with open("write-students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow((name, home))


with open("write-students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})
