from art import logo
from art import vs
from game_data import data
from replit import clear
import random
end_game=False
score=0
while end_game==False:
  print(logo)
  if score==0:
    compareA=random.randint(0,49)
  elif followA==followB:
    print(f"Es un empate! por lo que has ganado un punto. Tu puntaje es de: {score}")
    compareA=compareB
  else:  
    print(f"Correcto! Tu puntaje es de: {score}")
    compareA=compareB  
  compareB=random.randint(0,49)
  while compareB==compareA:
    compareB==random.randint(0,49)
  print(f"Compare: {data[compareA]['name']}, a {data[compareA]['description']} from {data[compareA]['country']}. ")
  print(vs)
  print(f"{data[compareB]['name']}, a {data[compareB]['description']} from {data[compareB]['country']}. ")
  choose= input("Who has more followers? Type 'A' or 'B': ").lower()
  followA=data[compareA]['follower_count']
  followB=data[compareB]['follower_count']
  if followA>followB and choose=="a":
    score+=1
    clear()
  elif followB>followA and choose=="b":
    score+=1
    clear()
  elif followA==followB:
    score+=1
    clear()
  else:
    clear()
    print(logo)
    print(f"Oh Oh-You lose! Tu puntaje final fue de: {score}.")
    end_game=True   
