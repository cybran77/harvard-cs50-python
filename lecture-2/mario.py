def main():
    # height = int(input("Height: "))
    # print_column(height)

    # row = int(input("Row: "))
    # print_row(row)

    print_square(3)


def print_column(height):
    # print("#\n" * height, end="")
    for _ in range(height):
        print("#")


def print_row(width):
    print("#" * width)


# def print_square(size):
#     for _ in range(size):
#         for _ in range(size):
#             print("#", end="")
#         print()
def print_square(size):
    for _ in range(size):
        print_row(size)


main()
