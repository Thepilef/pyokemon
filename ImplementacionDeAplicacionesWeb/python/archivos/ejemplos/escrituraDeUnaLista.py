#En este ejemplo, se crea una lista de nombres y se escriben 
#en el archivo nombres.txt, cada uno en una línea distinta.

nombres = ["ana", "luis", "pedro", "maria"]

with open("nombres.txt","w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n") 

print("los nombres se han guardado en 'nombres.txt'")