# names = []

# for _ in range(3):
#     names.append(input("What is your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}!")

# name = input("What is your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}!")

# names = []

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"Hello, {name}!")
