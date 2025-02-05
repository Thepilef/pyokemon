#pide al usuario una contraseña y verifica si es igual a "secreto123".
#si es correcto, imprime:
# "Acceso concedido"
#si no, imprime:
# "contraseña incorrecta"

contraseña = input("ingrese la contraseña: ")

if contraseña == "contraseña123":
    print("Acceso concedido")
else:
    print("contraseña incorrecta")