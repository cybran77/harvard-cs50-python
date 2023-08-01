def main():
    x = int(input("What's x? "))

    if isEven(x):
        print("x is even")
    else:
        print("x is odd")


def isEven(n) -> bool:
    # return True if n % 2 == 0 else False
    return n % 2 == 0


main()
