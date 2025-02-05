#pide al usuario un numero del 1 al 7 y muestra el dia de la semana correspondiente:
# 1: Lunes
# 2: Martes
# 3: Miercoles
# 4: jueves
# 5: Viernes
# 6: Sabado
# 7: Domingo
# si el numero no esta dentro de el rango:
# "numero fuera de rango"

numero = int(input("escriba un numero entre el 1 y el 7: "))

if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miercoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sabado")
elif numero == 7:
    print("Domingo")
else:
    print("numero fuera de rango")