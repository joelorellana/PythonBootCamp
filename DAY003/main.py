# PROJECT DAY 03: TREASURE ISLAND TEXT GAME
print('''
*******************************************************************************

                          o
                 o       /
                  \     /
                   \   /
                    \ /
               ______________
              |.------------.|
              ||            ||
              ||            ||
              ||            ||
              ||            ||
              ||____________||_
              |OO ....... OO | `-.
              '------_.-._---' _.'  
               _____||   ||___/_
              /  _.-|| N ||-._  \      .-._
             / -'_.---------._'- \    ,'___i--i___
            /_.-'_  NINTENDO _'-._\  ' /_+  o :::_\
           |`-i /m\/m\|\|/=,/m\i-'|  | || \ O / ||
       akg |  |_\_/\_/___\_/'./|  |  | \/  \ /  \/
            `-'              '-.`-'  ,      V
                                `---' 
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
decision1=input("Where do you want to start your journey? (type left or right) ").lower()
if decision1 == "left":
  print("OKAY! Now you're playing with Power! Choose your next destiny")
  print("Do you want to swim or wait for another activity?")
  decision2=input("Type swim or wait: ").lower()
  if decision2=="wait":
    print("Oh Look! There are three doors in front of you, choose your next destiny")
    decision3=input("Select a door: red, yellow or blue. ").lower()
    if decision3=="red":
      print("Oh, there is the direct path to HELL. Game Over.")
    elif decision3=="yellow":
      print("You WIN!!!!! CONGRATS")
    elif decision3=="blue":
      print("You were eaten by a Rathalos. GAME OVER")
    else:
      print("GAME OVER")   
  else:
    print("There is a giant octopus in the sea. GAME OVER")
else:
  print("You fall into a big hole, GAME OVER")
