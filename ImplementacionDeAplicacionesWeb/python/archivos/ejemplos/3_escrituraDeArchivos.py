#escribir texto en un archivo:
with open("salida.txt", "w") as archivo:
    archivo.write("esta es una linea de texto.\n")
    archivo.write("Otra linea de texto.\n")

#agregar texto al final de un archivo existente:
with open("salida.txt", "a") as archivo:
    archivo.write("esta linea se agrega al final del archivo.\n")

