import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    print(s)
    # hours = re.search(r"^(1[0-2]|0?[1-9]):[0-5][0-9]$", s)
    hours = re.search(r"/((1[0-2]|0?[1-9]):[0-5][0-9])/", s)
    print(hours)
    # print(hours.group(1))
    # print(hours.group(2))


if __name__ == "__main__":
    main()
