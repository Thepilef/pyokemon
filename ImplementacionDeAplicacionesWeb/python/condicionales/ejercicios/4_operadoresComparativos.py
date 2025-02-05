#pide al usuario dos numeros. usa condicionales para imprimir:
#
# "el primer numero es mayor que el segundo"
# "el segundo numero es mayor que el primero"
# "ambos numeros son iguales"


numero1 = int(input("escriba el numero1: "))
numero2 = int(input("escriba el numero2: "))

if numero1 > numero2:
    print("el primer numero es mayor que el segundo")
elif numero1 < numero2:
    print("el segundo numero es mayor que el segundo")
else:
    print("ambos numeros son iguales")