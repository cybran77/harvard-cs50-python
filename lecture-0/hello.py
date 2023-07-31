# Ask user for user's name
name = input("What's your name? ").strip().title()

# Greet user
print("hello \"friend\",", end=" ")
print(name, end="!\n")
print(f"hello, {name}!")
