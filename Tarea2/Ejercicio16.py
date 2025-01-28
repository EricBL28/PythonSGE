respuesta= str(input("¿Está lloviendo?\n"))

respuesta.lower()

if respuesta =="si":
    respuesta=str(input("¿Hace viento?\n"))
    respuesta.lower()
    if respuesta=="si":
        print("Hace demasiado viento para llevar un paraguas")
    elif respuesta == "no":
        print("Lleve un paraguas")

elif respuesta=="no":
    print("Disfrute del dia")

