letra=input("Escribe la primera linea de una cancion\n")
try:

    numeroInicial=int(input("Introduce numero inicial\n"))
    numeroFinal=int(input("Introduce numero final\n"))

    print("Parte del texto selecionada : "+letra[numeroInicial+1:numeroFinal])

except ValueError:
    print("No has introducido un numero")