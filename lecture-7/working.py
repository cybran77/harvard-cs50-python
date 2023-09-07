import re

# import sys


def main():
    print(convert(input("Hours: ")))


def review_format(s):
    pattern = r"((1[0-2]|0?[1-9])(:[0-5][0-9])|(1[0-2]|0?[1-9])) (?:AM|PM) to ((1[0-2]|0?[1-9])(:[0-5][0-9])|(1[0-2]|0?[1-9])) (?:AM|PM)"
    result = re.search(pattern, s)

    if result is None:
        raise ValueError("Invalid format")


def convert(s):
    format = review_format(s)

    pattern = r"((1[0-2]|0?[1-9])(:[0-5][0-9])? (?:AM|PM))"
    matches = re.findall(pattern, s)

    hours = [match[0] for match in matches]
    print(hours)
    if ":" in hours[0]:
        start_hour, start_minutes = hours[0].split(":")
        start_hour = convert_hour(start_hour, start_minutes[-2:])
        start_minutes = start_minutes.replace(" AM", "").replace(" PM", "")
    else:
        start_hour = hours[0]
        start_hour = convert_hour(
            start_hour.replace(" AM", "").replace(" PM", ""), start_hour[-2:]
        )
        start_minutes = "00"

    if ":" in hours[1]:
        end_hour, end_minutes = hours[1].split(":")
        end_hour = convert_hour(end_hour, end_minutes[-2:])
        end_minutes = end_minutes.replace(" PM", "").replace(" AM", "")
    else:
        end_hour = hours[1]
        end_hour = convert_hour(
            end_hour.replace(" AM", "").replace(" PM", ""), end_hour[-2:]
        )
        end_minutes = "00"

    result = f"{start_hour}:{start_minutes} to {end_hour}:{end_minutes}"
    # print(result)
    return result


def convert_hour(hour, meridiem):
    # print(hour, meridiem)
    if meridiem == "AM" and hour == "12":
        result = 0
    elif meridiem == "AM" and hour != "12":
        result = int(hour)
    elif meridiem == "PM" and hour != "12":
        result = int(hour) + 12
    else:
        raise ValueError("Invalid start hour")

    # print(result)
    return "{:02d}".format(result)


if __name__ == "__main__":
    main()
