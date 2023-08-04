# value error
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x must be an integer")

print(f"x is {x}")
