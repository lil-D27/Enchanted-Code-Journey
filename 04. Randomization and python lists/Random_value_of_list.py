import random

#seed
test_seed = input("Enter a seed value:") 
random.seed(test_seed) 
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

n = len(names)
random = random.randint(0, n-1)
print (f" {names[random]} is going to buy the meal today!")
