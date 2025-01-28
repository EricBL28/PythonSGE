try:
    respuesta= int(input("¿Que edad tienes?\n"))

    if respuesta >17:
        print("Puedes votar")
    elif respuesta ==17:
        print("Puedes aprender a conducir")
    elif respuesta==16:
        print("Puedes comprar lotería")
    elif respuesta<0:
        print("Edad no posible")
    else:
        print("Truco o trato")
except ValueError:
    print("Edad introducida no es un numero")

