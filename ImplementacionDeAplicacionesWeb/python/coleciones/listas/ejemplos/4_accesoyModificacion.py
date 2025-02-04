miLista = [1, "uno", 2, 3, 4, 5, 6, 7, 8, 9]
print(miLista)

#acceso por indice
elemento = miLista[0]   #Obtiene el primer elemento
print(elemento)
miLista[1] = 42         #Modifica el segundo elemento
print(miLista)

#acceso por rebanado (slicing) 
sub_lista = miLista[1:4]  #se incluye el primer el indice pero el ultimo no
print(sub_lista)