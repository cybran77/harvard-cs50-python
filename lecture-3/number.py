# value error
try:
    x = int(input("What's x? "))
except ValueError:
    print("x must be an integer")
else:
    print(f"x is {x}")
