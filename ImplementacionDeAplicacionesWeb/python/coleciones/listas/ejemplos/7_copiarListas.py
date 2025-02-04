import copy

miLista = [12, 1, -1, 0, 42, -43, 4, 54, 6, [27, 68, 943]]

#crea una copia superficial de la lista
#la lista que esta anidada sigue siendo la misma para miLista y para copiaLista
#por lo que para lista anidada apunta al mismo espacio en memoria
copiaLista = miLista.copy()
print(copiaLista)

#crea una copia independiente totalmente
#la sublista en este caso apunta a otro lugar en el almacenamiento

copiaCompleta = copy.deepcopy(miLista)
print(copiaCompleta)
