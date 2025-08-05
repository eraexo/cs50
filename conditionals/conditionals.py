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


# Score grading system
score = int(input("Enter your score: "))
if (score >= 90 and score <= 100):
    print("Grade: A")
elif (score >= 80 and score < 90):
    print("Grade: B")
elif (score >= 70 and score < 80):
    print("Grade: C")
elif (score >= 60 and score < 70):
    print("Grade: D")
elif (score >= 0 and score < 60):
    print("Grade: F")
else:
    print("Invalid score entered. Please enter a score between 0 and 100.")


# Even or odd number check
number = int(input("Enter a number to check if it's even or odd: "))
if (number % 2 == 0):
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Return true or false based on even or odd check
def check_even_odd(num):
    return num % 2 == 0


# Match case example
def match_case_example(value):
    match value:
        case "Harry" | "Hermione" | "Ron":
            return "Griffindor"
        case "Draco" | "Pansy" | "Vincent":
            return "Slytherin"
        case "Cedric" | "Cho":
            return "Hufflepuff"
        case "Luna" | "Neville":
            return "Ravenclaw"
        case _:
            return "Unknown House"

