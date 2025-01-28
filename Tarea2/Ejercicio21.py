nombre=str(input("Introduce solo tu nombre\n"))
apellidos=str(input("Introduce solo tus apellidos\n"))

nombre_completo=(nombre+" "+apellidos)
print(nombre_completo)

letras=int(nombre_completo.replace(" ","").__len__())

print("Tu nombre tiene "+str(letras)+" letras")