miLista = [1, "uno", 2, 3, 4, 5, 6, 7, 8, 9]
print(miLista)

#Elimina el primer elemento con el valor especifico
miLista.remove("uno")
print(miLista)

#Elimina y devuelve el elemento en la posicion especificada.
#Si no se especifica un indice, elimina el ultimo elmento.
miLista.pop(8)
print(miLista)

#Elimina todos los elementos de la lista
miLista.clear()
print(miLista)
