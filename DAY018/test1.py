def descendente(numero):
    if numero ==0:
        return ""
    else:
        print(numero)
        descendente(numero-1)
descendente(5)