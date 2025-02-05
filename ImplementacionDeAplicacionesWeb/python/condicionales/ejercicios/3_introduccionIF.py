#delcara una variable con un numero cualquiera. si el numero es positivo,
#imprime:
# "el numero es positivo"
#si el numero es negativo, imprime:
# "el numero es negativo"
#si el nuemero es 0, imprime:
# "el numero es cero"

numero = int(input("escribe un numero cualquiera: "))

if numero > 0:
    print("el numero es positiivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print("el numero es 0")