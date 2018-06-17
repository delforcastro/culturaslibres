pregunta = input("Ingrese F si quieren cargar Farenheit, o C si quiere cargar Celsius")

if pregunta == "F":
    grados = float(input ("Ingrese los grados Farenheit"))
    celsius = (grados - 32) * 5/9
    print ("El equivalente a " + str(grados) + " grados Ferenheit es " + str(celsius) + " grados Celsius")
else:
    grados = float (input("Ingrese los grados Celsius"))
    far = (grados * 9/5) + 32
    print ("El equivalente a " + str(grados) + " grados Celsius es " + str(far) + " grados Farenheit")
