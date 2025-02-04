#para evitar errores y manejar excepciones al trabajar con archivos, 
#se recomienda el uso de bloques try-except

try:
    with  open("archivo_que_no_existe.txt","r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
except Exception as e:
    print(f"ocurrio un error: {e}")