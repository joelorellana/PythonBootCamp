from menu import MENU
from menu import resources


def requeriments(coffee_type):
    #mejorar esta parte con un for
    if resources['water'] > MENU[coffee_type]['ingredients']['water']:
        if resources['coffee'] > MENU[coffee_type]['ingredients']['coffee']:
            if coffee_type == "cappuccino":
                if resources['milk'] > MENU[coffee_type]['ingredients']['milk']:
                    return True
                else:
                    print("Hace falta leche.")
                    return False
            else:
                return True
        else:
            print("Hace falta café.")
            return False
    else:
        print("Hace falta agua.")
        return False


def coffee_state(coffee):
    for i in resources:
        if coffee == "espresso" and i == "milk":
            continue
        resources[i] -= MENU[coffee]["ingredients"][i]


def payment(coffee):
    print("Por favor, ingrese las monedas necesarias para realizar su pago.")
    money = {"quarters": 0.25,
             "dimes": 0.10,
             "nickles": 0.05,
             "pennies": 0.01
             }
    total = 0.00
    for key in money:
        total += float(input(f"Ingrese el numero total de {key} (con un valor de {money[key]}): "))*money[key]
        print(f"Total ingresado: ${total:.2f}")
    if total == MENU[coffee]['cost']:
        print(f"Ha ingresado la cantidad correcta. Aquí está su {coffee}.")
        return total
    elif total > MENU[coffee]['cost']:
        change = total-MENU[coffee]['cost']
        print(f"Aquí está su café {coffee} y un cambio de ${change:.2f}")
        return MENU[coffee]['cost']
    else:
        print(f"Ha ingresado una cantidad insuficiente, se le regresarán los ${total}. Puede volver a intentarlo sí desea.")
        return 0


def report():
    for i in resources:
        print(f"{i}: {resources[i]}")
    print(f"Money: ${gains:.2f}")


gains = 0
start_coffee = True
coffee_type = ""
while start_coffee:
    start_menu = input("Qué desea preparar hoy? Type 'e' for espresso, 'l' for latte or 'c' for cappuccino: ").lower()
    if start_menu == "e":
        coffee_type = "espresso"
    elif start_menu == "l":
        coffee_type = "latte"
    elif start_menu == "c":
        coffee_type = "cappuccino"

    if coffee_type == 'espresso' or coffee_type == 'latte' or coffee_type == 'cappuccino':
        is_Possible = requeriments(coffee_type)
        if is_Possible:
            gains += payment(coffee_type)
            coffee_state(coffee_type)
        else:
            print("Por el momento no es posible hacerlo.")
        coffee_type = ""
    elif start_menu == 'off':
        print("Gracias por usar la cafetera. Hasta la próxima.")
        start_coffee = False
    elif start_menu == 'report':
        report()
    else:
        print("Introduzca un valor correcto.")
