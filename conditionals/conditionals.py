# User input for comparing two numbers
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

# Conditional statements to compare two numbers    
if (x > y):
    print(f"{x} is greater than {y}")
elif (x < y):
    print(f"{x} is less than {y}")
else:
    print(f"{x} is equal to {y}")


# Conditional with logical operator
if (x > y) or (x == y):
    print(f"{x} is either greater than or equal to {y}")
else:
    print(f"{x} is less than {y}")

