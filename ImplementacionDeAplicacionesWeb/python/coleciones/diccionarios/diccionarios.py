#Un diccionario es una colección desordenada de pares clave-valor. Cada clave es única y se usa para acceder a su valor correspondiente.
#Características:
#Desordenados.
#Modificables.
#Las claves deben ser únicas.

# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceder a valores por clave
print(mi_diccionario["nombre"])  # Salida: Juan

# Modificar un valor
mi_diccionario["edad"] = 26
print(mi_diccionario)  # Salida: {"nombre": "Juan", "edad": 26, "ciudad": "Madrid"}

# Agregar un nuevo par clave-valor
mi_diccionario["profesión"] = "Ingeniero"
print(mi_diccionario)

# Eliminar un par clave-valor
mi_diccionario.pop("ciudad")
print(mi_diccionario)