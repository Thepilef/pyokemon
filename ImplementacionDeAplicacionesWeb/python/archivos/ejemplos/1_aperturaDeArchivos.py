#apertura de archivos
#para abrir un archivo en python se utiliza la funcion integrada open(). la sintaxis basica es:
# archivo = open(nombre_archivo, modo)

#modos comunes de apertura
# r: modo de lectura. genera un errorsi el archivo no existe
#   ejemplo archivo = open("datos.txt", "r")  

# w: mode de escritura. crea el archivo si no existe o sobrescribe si ya existe
#   ejemplo archivo = open("datos.txt", "w")  

# a: mode de anexado. agrega contenido al final del archivo sin sobrescribirlo
#   ejemplo archivo = open("datos.txt", "a")  

# x: crea un archivol. genera un error si el archivo ya existe
#   ejemplo archivo = open("datos.txt", "x")  

