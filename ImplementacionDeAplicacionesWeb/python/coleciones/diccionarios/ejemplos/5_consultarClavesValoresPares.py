miDiccionario = {
    "nombre": "Andres",
    "edad": 21,
    "ciudad": "Madrid"
}

#keys(): no recibe parametros y devuelve una vista de las claves del diccionario
claves = miDiccionario.keys()
print(claves)

#values(): no recibe parametros y devuelve una vista de todos los valores del diccionario
values = miDiccionario.values()
print(values)

#items(): no recive parametros y devuelve un objeto dict_items, que se comporta
#como un conjunto (set-like) de tuplas (clave-valor)

items = miDiccionario.items()
print(items)
