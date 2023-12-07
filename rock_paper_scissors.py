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

game_images = [rock, paper, scissors]

#Write your code below this line 👇
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_choice = random.randint(0, 2)
# print(f"Computer chose {computer_choice}")

if user_choice == computer_choice:
    print("User choose:\n")
    print(game_images[user_choice])
    print("Computer choose:\n")
    print(game_images[computer_choice])
    print("You are Tied!")
else:
    if (user_choice == 0 and computer_choice == 2) or \
        (computer_choice == 0 and user_choice == 2):
        print("User choose:\n")
        print(game_images[user_choice])
        print("Computer choose:\n")
        print(game_images[computer_choice])
        print("Rock Wins!")
    elif (user_choice == 2 and computer_choice == 1) or \
        (computer_choice == 2 and user_choice == 1):
        print("User choose:\n")
        print(game_images[user_choice])
        print("Computer choose:\n")
        print(game_images[computer_choice])
        print("Scissors Wins!")
    elif (user_choice == 1 and computer_choice == 0) or \
        (computer_choice == 1 and user_choice == 0):
        print("User choose:\n")
        print(game_images[user_choice])
        print("Computer choose:\n")
        print(game_images[computer_choice])
        print("Paper Wins!")

