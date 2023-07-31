# Ask user for user's name
name = input("What's your name? ").strip().title()

# Split name into first and last name
first, last = name.split(" ", 1)

# Greet user
print(f"hello, {first} {last}!")
