#En este ejemplo, se busca una palabra especificada por el usuario en 
#el archivo articulo.txt y se cuenta cuántas veces aparece, sin distinguir 
#entre mayúsculas y minúsculas.

palabra_buscada = input("introduce la palabra a buscar: ")
contador = 0

with open("datos.txt","r") as archivo:
    for linea in archivo:
        contador += linea.lower().count(palabra_buscada.lower())

print(f"la palabra '{palabra_buscada}' aparece {contador} veces en el archivo")

