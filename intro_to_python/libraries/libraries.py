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
