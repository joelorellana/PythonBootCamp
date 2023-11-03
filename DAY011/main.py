# PROJECT: BLACKJACK card game

import random
from replit import clear
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def dealer(mazo):
  """ Establece una función que permita tomar las cartas para el dealer"""
  dealer_cards=random.choices(mazo,k=2)
  if sum(dealer_cards)==22:
    dealer_cards[dealer_cards.index(11)]=1
  elif sum(dealer_cards)==21:
    return dealer_cards
  while sum(dealer_cards)<=17:
    dealer_cards.append(random.choice(mazo))
    if sum(dealer_cards)>21 and dealer_cards.count(11)>=1:
      dealer_cards[dealer_cards.index(11)]=1
  return dealer_cards
def player(mazo):
  """ Establece una función que permita tomar las cartas para el jugador"""
  player_cards=random.choices(mazo,k=2)
  if sum(player_cards)==22:
    player_cards[player_cards.index(11)]=1
  elif sum(player_cards)==21:
    return player_cards
  game_continue= True
  while game_continue:
    print(f"Tus cartas son: {player_cards}, suma: {sum(player_cards)}")
    print(f"La primera carta del CPU es: {cpu[0]}")
    next_move= input("Desea tomar otra carta? type 'y' for yes or another letter for pass: ").lower()
    if next_move=="y":
      player_cards.append(random.choice(mazo))
      if sum(player_cards)>21 and player_cards.count(11)>=1:
        player_cards[player_cards.index(11)]=1
      if sum(player_cards)>21:
        game_continue=False  
    else:
      game_continue= False   
  return player_cards
def game_rules(player,dealer):
  if sum(player)>21:
    print("CPU wins.")
  elif sum(player)==21 and len(player)==2 and sum(dealer)!=21:
    print("You win with a Blackjack.")
  elif sum(dealer)==21 and len(dealer)==2 and sum(player)!=21:
    print("The CPU win with a Blackjack.")    
  elif sum(player)<=21 and sum(player)>sum(dealer):
    print("You win.")
  elif sum(player)<=21 and sum(dealer)>21:
    print("You win.")
  elif sum(player)<=21 and sum(dealer)>sum(player):
    print("CPU wins.")  
  else:
    print("It's a tie.")
game_start= True
while game_start:
  jugar= input("Deseas jugar una partida de Blackjack? type 'y' for yes or 'n' for no: ").lower()
  if jugar=="y":
    clear()
    print(logo)
    cpu= dealer(cards)
    gamer=player(cards)
    print(f"CPU cartas finales: {cpu}, suma final: {sum(cpu)}." )
    print(f"Tus cartas finales fueron: {gamer}, suma final: {sum(gamer)}")
    game_rules(gamer,cpu)
  elif jugar=="n":
    game_start=False
  else:
    print("Ha introducido un valor incorrecto. Intente de nuevo.")
