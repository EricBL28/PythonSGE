
try:

    num=int(input("Introduce un numero entre 10 y 20(ambos inclusive)\n"))

    if 21 > num > 9:
        print("Gracias")
    else:
        print("Respuesta incorrecta")


except ValueError:
    print("No es un numero")