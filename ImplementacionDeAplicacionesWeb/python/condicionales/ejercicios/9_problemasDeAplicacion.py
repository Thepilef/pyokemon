#pide al usuario una temperatura en grados celcius. si la temperatura es:
# mayor o igual a 30: imprime "Hace calor"
# entre 10 y 29; imprime "El clima es templado"
# menor a 10: imprime "Hace frio"


numero = int(input("dame una temperatura en grados celcius: "))

if numero >= 30:
    print("Hace calor")
elif numero >= 10 and numero <= 29:
    print("el clima es templado")
else:
    print("hece frio")