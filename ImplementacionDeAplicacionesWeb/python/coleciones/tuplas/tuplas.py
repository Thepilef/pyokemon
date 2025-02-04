#Una tupla es una colección ordenada pero inmutable (no puede ser modificada después de su creación).
#Características:
#Ordenadas.
#Inmutables.
#Permiten duplicados.

# Crear una tupla
mi_tupla = (1, 2, 3, 4, 5)

# Acceder a elementos
print(mi_tupla[0])  # Salida: 1

# Intentar modificar un elemento (provoca un error)
# mi_tupla[1] = 10  # TypeError

# Usar tuplas para valores constantes
coordenadas = (10.0, 20.0)
print(coordenadas)  # Salida: (10.0, 20.0)