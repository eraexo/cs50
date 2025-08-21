# Exceptions
x_value = int(input("Insert x: "))
print(f"Value of x is: {x_value}")

# Try and Expect
while True:
    try:
        x_value = int(input("Insert x: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer for x.")

print(f"Value of x is: {x_value}")

# Function to get x value with error handling
def main():
    x_value = get_x_value()
    print(f"Value of x is: {x_value}")

def get_x_value():
    while True:
        try:
            x_value = int(input("Insert x: "))
            return x_value
        except ValueError:
            print("Invalid input! Please enter a valid integer for x.")

if __name__ == "__main__":
    main()