conjunto1 = {1, 2, 3}
conjunto2 = {3, 5, 6}
print(conjunto1)
print(conjunto2)

#union(| o union)
union = conjunto1 | conjunto2
print(union)

union1 = conjunto1.union(conjunto2)
print(union1)

#interseccion (& o interseccion)
interseccion = conjunto1 & conjunto2
print(interseccion)
interseccion1 = conjunto1.intersection(conjunto2)
print(interseccion1)

#diferencia (- o diferencia)
diferencia = conjunto1 - conjunto2
print(diferencia)
diferencia1 = conjunto1.difference(conjunto2)
print(diferencia1)

#diferencia simetrica (^ o symmetric_difference)
diferenciaSimetrica = conjunto1 ^ conjunto2
print(diferenciaSimetrica)
diferenciaSimetrica1 = conjunto1.symmetric_difference(conjunto2)
print(diferenciaSimetrica1)
