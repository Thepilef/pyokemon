#implementa un programa que copie el contenido de un archivo llamado
#origen.txt a un archivo llamado destino.txt

with open("origen.txt","r") as origen:
    contenido = origen.read()

with open("destino.txt","w") as destino:
    destino.write(contenido)
