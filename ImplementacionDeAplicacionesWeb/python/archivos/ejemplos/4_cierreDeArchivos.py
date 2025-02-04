#aunque python cierra automaticamente los archivos al salir del bloque with,
#es una buena practica cerrarlos manualmente si no se utiliza with:

archivo = open("datos.txt","r")
contenido = archivo.read()
print(contenido)
archivo.close()