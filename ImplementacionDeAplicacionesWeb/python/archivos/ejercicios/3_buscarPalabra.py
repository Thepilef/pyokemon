#diseña un programa que busque una palabra dada por el usuario
#dentro de un archivo llamado notas.txt e indique cuantas
#veces aparece

palabra = input("introduce una palabra para buscarla en el documento: ")
contador = 0

with open("notas.txt","r") as archivo:
    
    for linea in archivo:
        contador += linea.lower().count(palabra.lower())

print(contador)