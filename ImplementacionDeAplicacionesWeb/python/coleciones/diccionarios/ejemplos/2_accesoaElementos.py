miDiccionario = {
    "nombre": "Andres",
    "edad": 21,
    "ciudad": "Madrid"
}

#acceder a un valor mediante su clave
nombre = miDiccionario["nombre"]
print(nombre)

#usar get(clave, valor por defecto) para evitar errores
genero = miDiccionario.get("genero", "no especificado")
print(genero)
ciudad = miDiccionario.get("ciudad", "no espedificado")
print(ciudad)
