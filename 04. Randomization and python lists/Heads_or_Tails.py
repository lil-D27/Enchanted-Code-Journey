#Generating random value with seed

#seed - generates random number from any equation or value
# - we can use Geiger Counter to generate random numbers

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0,1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")
