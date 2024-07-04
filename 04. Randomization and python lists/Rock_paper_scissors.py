import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]
player_choice = int(input("What do you choose? 'rock' - 0 , 'paper' - 1 , or 'scissors' - 2\n")) 
print ("You chose:")
print(list[player_choice])

random_i = random.randint(0, 2)
computer_choice = list[random_i]
print ("Computer chose:\n")
print(computer_choice)

if player_choice == rock:
    if computer_choice == rock:
        print("It's a tie")
    elif computer_choice == paper:
        print("You lose")
    else:
        print("You win")
elif player_choice == paper:
    if computer_choice == rock:
        print("You win")
    elif computer_choice == paper:
        print("It's a tie")
    else:
        print("You lose")
else:
    if computer_choice == rock:
        print("You lose")
    elif computer_choice == paper:
        print("You win")
    else:
        print("It's a tie")
