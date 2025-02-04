miConjunto = {1, 2, 3, 4, 5}
print(miConjunto)

#add(x): agrega un elemento al conjunto
miConjunto.add(6)
print(miConjunto)

#remover(x): elimina un elemento. lanza un error si el elemento no esta 
#presente y termina la ejecucion del codigo
miConjunto.remove(6)
print(miConjunto)
# miConjunto.remove(7)

#discard(x): elimina un elemento sin lazar el erros si no esta presente
miConjunto.discard(7)
print(miConjunto)

#pop(): elimina y devuelve un elemento aleatorio del conjunto
elemento = miConjunto.pop()
print(elemento)
print(miConjunto)

#clear(): elimina todos los elementos del conjunto
miConjunto.clear()
print(miConjunto)