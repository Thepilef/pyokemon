cadena = "Hola a todos"

cadenaSinEspacios = ""

for letra in cadena:
    if letra not in " ":
        cadenaSinEspacios += letra
        print(cadenaSinEspacios)
