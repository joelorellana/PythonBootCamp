# PROJECT: GUESS THE NUMBER
import random
from art import logo
guess =random.randint(1,100)
def compare(number):
  if number>guess:
    return "Too much high"
  elif number<guess:
    return "Too much low"
  else:
    return "You win."
def difficulty():
  user_input=input("inserte el nivel de dificultad que desea para el juego, 'easy' para 10 vidas o 'hard' para 5 vidas: \n").lower()
  if user_input=="easy":
    return 10
  elif user_input=="hard":
    return 5
  else:
    return difficulty()
print(logo)
print("Welcome to the Guess Number Game, made by JoelDev89. ")
start_game=True
  game_life=difficulty()
  while game_life>0:
    if game_life==1:
      print("Tienes solo 1 vida disponible.")
    else:
      print(f"Tienes {game_life} vidas disponibles.")
    user_number=int(input("Introduce un numero del 1 al 100: \n"))
    resultado=compare(user_number)
    print(resultado)
    if resultado=="You win.":
      print(f"Felicidades, el número era: {guess}")
      break
    else:
      game_life-=1
if game_life==0:
  print("Lo sentimos mucho, más suerte a la próxima.")
