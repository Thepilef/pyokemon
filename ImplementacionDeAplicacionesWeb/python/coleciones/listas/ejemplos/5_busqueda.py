miLista = [1, 1, 1, "uno", 2, 3, 4, 5, 6, 7, 8, 9]
print(miLista)

#sintaxis
# index(x , start, end)
# x es el valor que quieres buscar y es obligatorio
# start es el indice por el cual quieres comenzar a buscar y es opcional
# end es el indice hasta el que quieres buscar y es opcional

#devuelve el indice del primer elemento con el valor especifico
ejemplo = miLista.index(1)
print(ejemplo)


#Count() devuelve el numero de veces que un valor aparece en la lista
repetidos = miLista.count(1)
print(repetidos)