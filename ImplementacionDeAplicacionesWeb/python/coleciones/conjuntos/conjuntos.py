#Un conjunto es una colección desordenada y sin índices que no permite elementos duplicados.
#Características:
#Desordenados.
#No permiten duplicados.
#Modificables. 

# Crear un conjunto
mi_conjunto = {1, 2, 3, 4, 5}

# Agregar elementos
mi_conjunto.add(6)
print(mi_conjunto)  # Salida: {1, 2, 3, 4, 5, 6}

# Intentar agregar un duplicado (no tiene efecto)
mi_conjunto.add(3)
print(mi_conjunto)  # Salida: {1, 2, 3, 4, 5, 6}

# Eliminar elementos
mi_conjunto.remove(2)
print(mi_conjunto)  # Salida: {1, 3, 4, 5, 6}