miDiccionario = {
    "nombre": "Andres",
    "edad": 21,
    "ciudad": "Madrid",
    "genero": "Masculino"
}

#pop(clave, valor por defecto): elimina una clave y devuelve su valor
#si no existe y no se espesifica un valor por defecto, lanza un error
miDiccionario.pop("genero")
print(miDiccionario)

eliminarInexistente = miDiccionario.pop("genero", "noExiste")
print(eliminarInexistente)

#del diccionario[clave]: elimina una clave directamente
del miDiccionario["ciudad"]
print(miDiccionario)

#popitem(): elimina y devuelvce el ultimo par clave-valor añadido
#(util en verciones modernas de python)

ultimo = miDiccionario.popitem()
print(ultimo)
print(miDiccionario)

#clear(): elimina todos los elementos del diccionario
miDiccionario.clear()
print(miDiccionario)