# While loop
i = 3
while(i > 0):
    print("loop " + str(i))
    i -= 1
    
# For loop
for i in [0, 1, 2]:
    print("loop " + str(i))


# For loop with range
for i in range(3):
    print("loop " + str(i))

print("meow\n" * 3, end="")

# While loop with range
i = 0
while(i < 3):
    print("loop " + str(i))
    i += 1

# While loop with input
n = int(input("Enter a number: "))

while True:
    if n > 0:
        print("loop " + str(n))
        break

for _ in range(n):
    print("meow")


# While and for loop inside functions
def main():
    number = get_number()
    meow(number)

def get_number():
    n = int(input("Enter a number: "))
    while True:
        if n > 0:
            return n
        else:
            print("Please enter a positive number.")
            n = int(input("Enter a number: "))

def meow(n):
    for _ in range(n):
        print("meow")

if __name__ == "__main__":
    main()


# Iterate over a list
animals = ["cat", "dog", "bird"
           ]
for animal in animals:
    print("I have a " + animal)

print(len(animals))

def length_of_list(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

print(length_of_list(animals))

# iterate using len
def iterate_with_len(lst):
    for i in range(len(lst)):
        print("I have a " + lst[i])

iterate_with_len(animals)

# Dictionaries
animals_dict = {
    "cat": "meow",
    "dog": "woof",
    "bird": "tweet"
}

print(animals_dict)
print(animals_dict["cat"])


for animal, sound in animals_dict.items():
    print(f"The {animal} goes {sound}")

