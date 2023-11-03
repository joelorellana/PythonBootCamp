from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Bienvenido al programa de subastas creado por JoelDev89®")
hay_participantes = True
guia_personas={}
while hay_participantes:
  estado_subasta=input("Desea agregar un participante a la subasta? type 'yes' or 'no': ").lower()
  if estado_subasta=="yes":
    nombre=input("Ingrese el nombre de la persona: \n")
    cantidad=float(input("Cuanto será el valor que desea dar por la subasta? \n$"))
    guia_personas[nombre]= cantidad
  elif estado_subasta=="no":
    hay_participantes = False
  clear()  
cantidad_mayor=0
ganador=""    
if len(guia_personas)>0:
  for codigo in guia_personas:
    if guia_personas[codigo]>cantidad_mayor:
      cantidad_mayor=guia_personas[codigo]
      ganador=codigo
  print(f"La persona que ganó la subasta es {ganador} ya que ofreció la cantidad de {cantidad_mayor}")
else:
  print("No introdujo personas, por tanto no puede calcularse un ganador")    
