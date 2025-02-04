miTupla = (1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 5)
print(miTupla)

#devuelve cuantas veces aparece un valor en la tupla
ocurrencias = miTupla.count(2)
print(ocurrencias)

#index(x1, x2, x3) devuelve el primer elemento con el valor especificado
#x1 es el valor que estas buscando
#x2 es el indice en el que quieres comenzar la busqueda
#x3 es el indice en el que quieres que la busqueda termine

indice = miTupla.index(2, 2, 9)
print(indice)