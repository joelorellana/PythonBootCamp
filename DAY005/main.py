# PASSWORD GENERATOR PROJECT
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password=[]

for i in range(0,nr_letters):
  num_letra=random.randint(0, len(letters)-1) #numero de letra a tomar
  password.append(letters[num_letra])
for i in range(0,nr_symbols):
    num_symbol=random.randint(0, len(symbols)-1) #numero de simbolo a tomar
    password.append(symbols[num_symbol])
for i in range(0,nr_numbers):
    num_number=random.randint(0, len(numbers)-1) #numero de numero a tomar
    password.append(numbers[num_number])
random.shuffle(password)
random_pass="".join(password)
print(f"Your new password is {random_pass}")
