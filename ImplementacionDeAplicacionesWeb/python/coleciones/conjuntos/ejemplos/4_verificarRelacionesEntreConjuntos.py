conjunto1 = {1, 2, 3}
conjunto2 = {3, 5, 6}
print(conjunto1)
print(conjunto2)

#issubset(otro conjunto): comprueba si un conjunto es subconjunto de otro
issubset = {1, 2}.issubset({1, 2, 3, 4})
print(issubset)

issubset1 = conjunto1.issubset(conjunto2)
print(issubset1)

#issuperset(otro conjunto)
issuperset = {1, 2}.issuperset({1, 2, 3})
print(issuperset)

issuperset1 = conjunto1.issuperset(conjunto2)
print(issuperset1)

#isdisjoint(otro conjunto): comprueba si dos conjuntos no tienen elementos en comun
isdisjoint = {1, 2}.isdisjoint({3, 4})
print(isdisjoint)
isdisjoint1 = conjunto1.isdisjoint(conjunto2)
print(isdisjoint1)