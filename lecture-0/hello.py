def main():
    # Ask user for user's name
    name = input("What's your name? ").strip().title()
    sayHello(name)


def sayHello(to="world"):
    print(f"hello, {to}!")


main()
