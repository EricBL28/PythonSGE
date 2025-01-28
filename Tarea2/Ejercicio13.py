
try:

    num=int(input("Introduce un numero inferior a 20\n"))

    if num<20:
        print("Gracias")
    else:
        print("Demasiado alto")


except ValueError:
    print("No es un numero")