letra=input(print("Escribe la primera linea de una cancion"))
try:

    numeroInicial=int(input("Introduce numero inicial"))
    numeroFinal=int(input("Introduce numero final"))

except ValueError:
    print("No has introducido un numero")