# Get two numbers from the user
x = float(input("What's x? "))
y = float(input("What's y? "))

# Divide and round the result to two decimal places
z = round(x / y, 2)

# Print the result to the user
print(f"{z:.2f}")
