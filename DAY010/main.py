# CALCULATOR
from art import logo
#Calculator program
print(logo)
print("This program is made by JoelDev89®")
def suma(sum1,sum2):
  return sum1+sum2
def resta(minu,sustr):
  return minu-sustr
def producto(fac1, fac2):
  return fac1*fac2
def cociente (fac1, fac2):
  if fac2 !=0:
    return fac1/fac2
  else:
    return "La división entre cero es indefinida." 
def calculator():
  num1= float(input("Ingrese el primer número con el que desea realizar una operación:"))
  start_calc= True
  while start_calc:
    oper= input("Escriba el símbolo de la operación que desea realizar: ")
    if oper=="+" or oper=="-" or oper=="*" or oper=="/":
      num2= float(input("Ingrese el segundo numero: "))
      if oper=="+":
        resultado=suma(num1,num2)
      elif oper=="-":
        resultado=resta(num1,num2)
      elif oper=="*":
        resultado=producto(num1,num2)
      elif oper=="/":
        resultado=cociente(num1,num2)
      print(f"El resultado de la operación es: {resultado}")
      if type(resultado)== float:
        another_op=input("Si desea usar el resultado anterior, escriba 'c', Si desea hacer otra operacion, escriba: 'a', si desea salir de la calculadora, escriba 'q': ").lower()
        if another_op=="c":
          num1=resultado
        elif another_op=="q":
          start_calc = False
          print("Gracias por usar mi calculadora.")
        elif another_op=="a":
          calculator()  
        else:
          print("No se pudo interpretar su respuesta.")
          start_calc = False
      else:
        start_calc = False
        print("Vuelva a iniciar la calculadora para operar dos cantidades")              
    else:
      print("Ha ingresado una operación no válida")    
calculator()
