# names = []

# for _ in range(3):
#     names.append(input("What is your name? "))

# for name in sorted(names):
#     print(f"Hello, {name}!")

name = input("What is your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
