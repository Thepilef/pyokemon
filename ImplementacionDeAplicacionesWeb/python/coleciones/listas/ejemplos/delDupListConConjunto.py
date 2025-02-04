numeros = [1, 2, 2, 3, 4, 4, 5]

numeros_unicos = list(set(numeros))

print(numeros_unicos)

#El método set() convierte la lista en un conjunto, eliminando automáticamente 
#los duplicados porque los conjuntos no permiten elementos repetidos. Luego, la 
#función list() convierte el conjunto resultante de nuevo a una lista para mantener 
#la estructura original.