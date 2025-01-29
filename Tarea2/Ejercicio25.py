
nombre=input("Introdue tu nombre de pila\n")

if len(nombre)<5:
    apellido=input("Introduce tu apellido\n")
    nombre=" ".join([nombre,apellido]).upper()
    print(nombre)
else:
    nombre=nombre.lower()
    print(nombre)
