#python proporciona varias formas de leer archivos

#leer todo el contenido:
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#leer por linea:
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

#leer un numero especifico de caracteres:
with open("datos.txt", "r") as archivo:
    contenido = archivo.read(10)
    print(contenido)