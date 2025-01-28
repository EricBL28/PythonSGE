
try:

    num=int(input("Introduce un numero\n"))
    num2=int(input("Introduce otro numero\n"))

    if num<num2:
        print("\n"+str(num2))
        print(num)
    else:
        print("\n"+str(num))
        print(num2)

except ValueError:
    print("No es un numero")
