score = int(input("What's your score? "))

if 90 <= score <= 100:
    print("You got an A!")
elif 80 <= score < 90:
    print("You got a B!")
elif 70 <= score < 80:
    print("You got a C!")
elif 60 <= score < 70:
    print("You got a D!")
else:
    print("You got an F!")
