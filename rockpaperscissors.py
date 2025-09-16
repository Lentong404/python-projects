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

player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
# if player_input == 0:
#     print (rock)
# if player_input == 1:
#     print (paper)
# if player_input == 2:
#     print (scissors)

# Huh, the code doesnt account for if the player chooses something other than an integar
if player_input >= 3 and player_input < 0:
    print ("This is an invalid choice, you've lost :(!")
# If the if statement isnt used, and a number is chosen outside the listed numbers, itll return an index error
if player_input >= 0 and player_input <= 2:
    print(game_images[player_input])
# def square(n):
#   is_integer = isinstance(n,int)
#   assert is_integer,"input must be integer"

print(game_images[player_input])

computer_choice = random.randint(0, 2)
print ("Computer Chose:")
# if computer_choice == 0:
#     print (rock)
# if computer_choice == 1:
#     print (paper)
# if computer_choice == 2:
#     print (scissors)

# Player and Computer made the same choice
if player_input == computer_choice:
    print ("Its a tie!")
# Player = Rock
if player_input == 0 and computer_choice == 2:
    print ("You Won!")
if player_input == 0 and computer_choice == 1:
    print ("You Lost :(!")
# Player = Paper
if player_input == 1 and computer_choice == 0:
    print ("You Won!")
if player_input == 1 and computer_choice == 2:
    print ("You Lost :(!")
# Player = Scissors
if player_input == 2 and computer_choice == 0:
    print ("You Lost :(!")
if player_input == 2 and computer_choice == 1:
    print ("You Won!")