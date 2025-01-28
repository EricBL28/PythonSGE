try:
    respuesta= int(input("Introduce 1,2 o 3\n"))

    if respuesta==1:
        print("Gracias")
    elif respuesta==2:
        print("Bien hecho")
    elif respuesta==3:
        print("Correcto")
    else:
        print("Mensaje de error")

except ValueError:
    print("Numero introducido no es numero")
