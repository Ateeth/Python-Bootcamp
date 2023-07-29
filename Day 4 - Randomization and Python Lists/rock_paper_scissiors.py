## Rock Paper Scissors

# Instructions

# Make a rock, paper, scissors game.

# Inside the `main.py` file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: `rock`, `paper`, and `scissors`. This will make it easy to print them out to the console.

# Start the game by asking the player:

# *"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."*

# From there you will need to figure out:
# * How you will store the user's input.
# * How you will generate a random choice for the computer.
# * How you will compare the user's and the computer's choice to determine the winner (or a draw).
# * And also how you will give feedback to the player.

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

#Write your code below this line 👇
import random


user = int(input("Enter your choice : 0 for rock, 1 for Paper, 2 for Scissiors : "))

computer = random.randint(0 , 2)

print("User")
if user == 0 :
  print(rock)
elif user == 1 :
  print(paper)
elif user == 2 :
  print(scissors)

print("Computer")
if computer == 0 :
  print(rock)
elif computer == 1 :
  print(paper)
elif computer == 2 :
  print(scissors)

if ( user == 0 and computer == 2 ) or ( user == 1 and computer == 0 ) or ( user == 2 and computer == 1) :
  print("User is the winner !!!")
elif ( user == 2 and computer == 0 ) or ( user == 0 and computer == 1 ) or ( user == 1 and computer == 2) :
  print("Computer is the winner !!!")
else :
  print("Game is a draw !!")