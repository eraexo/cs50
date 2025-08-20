# Exceptions
x_value = int(input("Insert x: "))
print(f"Value of x is: {x_value}")

# Try and Expect
try:
    y_value = int(input("Insert y: "))    
except ValueError:
    print("Invalid input! Please enter a valid integer for y.")
    y_value = 0
else:
    print(f"Value of y is: {y_value}")