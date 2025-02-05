#pide al usuario un numero. si el numero esta entre 1 y 100 (inclusive),
#imprime:
# "el numero esta dentro del rango"
#si no, imprime
# "el numero esta fuera del rango"

numero = int(input("ingrese un numero: "))

if numero >= 1 and numero <= 100:
    print("el numero esta dentro del rango")
else:
    print("el numero esta fuera del rango")