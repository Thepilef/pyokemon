#escribe un programa que cuente cuantas lineas tiene
#un archivo de texto llamado poema.txt

with open("notas.txt","r") as archivo:
    contador = 0
    for linea in archivo:
        contador += 1

print(contador)