# import random
import random

# random choice
my_list = [1, 2, 3, 4, 5]
print(random.choice(my_list))

# print random heads or tails
print(random.choice(['heads', 'tails']))

# random integer
print(random.randint(1, 10))

# random shuffle
cards = ['A', 'K', 'Q', 'J', '10']
random.shuffle(cards)
print(cards)

# random statitics
import statistics
data = [1, 2, 3, 4, 5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.stdev(data))
print(statistics.variance(data))

# import sys
import sys
print(sys.version)
print(sys.platform)
print(sys.path)
print("Hello, there", sys.argv[1]) # Pass your name as a command line argument
print("Script name:", sys.argv[0]) # Script name
print("Number of arguments:", len(sys.argv)) # Number of arguments
print("Argument List:", str(sys.argv)) # Argument list

# try except with sys arguments
try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum:", num1 + num2)
except (IndexError, ValueError):
    print("Please provide two integers as command line arguments.")

# if conditional with sys arguments
if len(sys.argv) > 2:
    print("You have provided more than two arguments.")
elif len(sys.argv) < 2:
    print("You have provided less than two arguments.")
else:
    print("You have provided exactly two arguments.")

# for loop with sys arguments
for i in range(1, len(sys.argv)):
    print(f"Argument {i}: {sys.argv[i]}")

# sys with cowsay
import cowsay
cowsay.cow("Hello, " + sys.argv[1]) # Pass your name as a command line argument
cowsay.tux("This is Tux the Linux penguin!")
cowsay.dragon("Fear the dragon!")
cowsay.beavis("I am Beavis, heh heh.")
cowsay.cheese("I love cheese!")
cowsay.trex("Roar! I am a T-Rex!")

