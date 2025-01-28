nombres=str(input("Introduce solo tu nombre en minusculas\n"))
apellidos=str(input("Introduce solo tus apellidos en minusculas\n"))

nombre=nombres.split()
apellido=apellidos.split()

nombre_completo=""

for i in range(nombre.__len__()):
    nombreaux=nombre[i].capitalize()
    nombre[i]=nombreaux
    nombre_completo=nombre_completo+" "+nombre[i]

for i in range(apellido.__len__()):
    apellidoaux=apellido[i].capitalize()
    apellido[i]=apellidoaux
    nombre_completo = nombre_completo + " " + apellido[i]

print(nombre_completo.strip())



