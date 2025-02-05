#pide al usuario una letra. si la letra es una vocal (a, e, i, o, u),
#imprime:
# "es una vocal"
#si no, imprime:
# "no es una vocal"

letra = input("ingrese una letra: ")

if letra in ("a", "e", "i", "o", "u"):
    print("es una vocal")
else:
    print("no es una vocal")
