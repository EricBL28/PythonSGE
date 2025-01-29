vocales = "aeiou"

palabra = input("Introduce una palabra: ")
palabra = palabra.lower()

if palabra[0] in vocales:
    palabra=palabra + "way"
else:
    palabra=palabra[1:] + palabra[0] + "ay"

print("En latín porcino: ", palabra)
