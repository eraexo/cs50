# Hello world
print("hello world")

""" 
# Variables and input/output
name = input("What's your name? ")
print("My name is ", name)

# Escape characters
name = input("What's your name? ")
print("My name is \"", name, "\"")  # Using escape character for double quotes
print("My name is ", name, sep="\n")  # Using sep to go to a new line
print(f"My name is {name}")  # Using f-string for formatted output
"""

# Remove whitespace
name = input("What's your name? ")
print("My name is", name.strip().capitalize())  # Using strip() to remove leading/trailing whitespace and capitalize() to capitalize the first letter

# Addition
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is", num1 + num2)  # Adding two numbers and printing

# Functions with parameters
def greet(name="World"):
    print(f"Hello, {name}!")  # Function to greet a person

greet()  # Calling the function with default parameter
greet("Alice")  # Calling the function with a specific name