#crea un programa que lea el contenido de un archivo llamado notas.txt
#y lo imprima en la consola

with open("notas.txt","r") as archivo:
    contenido = archivo.read()

print(contenido)