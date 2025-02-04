#escribe un programa que toma una lista de nombres y los guarde en un
#archivo llamado nombres.txt, un nombre por linea

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

with open("numeros.txt","w") as archivo:
    for numero in numeros:
        archivo.write(str(numero) + "\n")

