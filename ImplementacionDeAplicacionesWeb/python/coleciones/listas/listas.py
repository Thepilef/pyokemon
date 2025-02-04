#Una lista es una colección ordenada y modificable que permite almacenar elementos duplicados.
#Características:
#Ordenadas.
#Modificables (mutable).
#Permiten duplicados.

# Crear una lista
mi_lista = [1, 2, 3, 4, 5]

# Acceder a elementos
print(mi_lista[0])  # Salida: 1

# Modificar elementos
mi_lista[1] = 10
print(mi_lista)  # Salida: [1, 10, 3, 4, 5]

# Agregar elementos
mi_lista.append(6)
print(mi_lista)  # Salida: [1, 10, 3, 4, 5, 6]

# Eliminar elementos
mi_lista.remove(10)
print(mi_lista)  # Salida: [1, 3, 4, 5, 6]