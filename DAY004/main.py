# DAY 04: ROCK, PAPER, SCISSORS GAME
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
print("Welcome to the Rock, Paper, Scissors: The Game")
player=int(input("What do you choose? Please type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
import random
cpu= random.randint(0,2)
list1=[rock, paper, scissors]
if player>0 and player<2:
  print(list1[player])
print("Computer chose: ")
print(list1[cpu])
if player==cpu:
  print("Even.")
elif (player==0 and cpu==1) or (player==1 and cpu==2) or (player==2 and cpu==0):
  print("Computer won")
elif (player==0 and cpu==2) or (player==1 and cpu==0) or (player==2 and cpu==1):
  print("You win")
else:
  print("You type an invalid number. You lose.")
