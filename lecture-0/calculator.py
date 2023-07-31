def main():
    x = float(input("What's x? "))
    print(f"The square of {x} is {square(x)}")


def square(n) -> float:
    return pow(n, 2)


main()
