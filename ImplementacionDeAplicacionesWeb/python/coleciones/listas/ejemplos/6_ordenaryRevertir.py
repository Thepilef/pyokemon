miLista = [12, 1, -1, 0, 42, -43, 4, 54, 6, 27, 68, 943]
miListastr = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho" ]
print(miLista)

#sort(reverse=false, key=none) ordena los elementos de la lista en su lugar
miLista.sort()
print(miLista)

miLista.sort(reverse=True)
print(miLista)

miLista.sort(key=abs)
print(miLista)

miListastr.sort(key=len)
print(miListastr)

miListastr.sort(key=str.lower)
print(miListastr)

#sorted(lista) devuelve una nuevo lista ordenada (sin modidficar la original)

nuevaLista = sorted(miLista)
print(nuevaLista)

#reverse(): invierte el orden de los elementos en la lista

nuevaLista.reverse()
print(nuevaLista)
