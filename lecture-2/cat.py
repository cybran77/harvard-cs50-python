# i = 0
# while i < 3:
#     print("meow")
#     i += 1
# print("purr\n" * 3, end="")


def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("Number of meows: "))
        if n > 0:
            return n


def meow(n):
    # print("meow\n" * n, end="")
    for _ in range(n):
        print("meow")


main()
