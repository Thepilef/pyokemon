miDiccionario = {
    "nombre": "Andres",
    "edad": 21,
    "ciudad": "Madrid"
}
print(miDiccionario)

miDiccionario1 = {
    "ciudad": "Bogota",
    "genero": "masculino"
}
print(miDiccionario1)

#update(otro diccionario): agregar los pares clave-valor de otro diccionario.
#si alguna clave ya existe, se sobrescribe su valor

miDiccionario.update(miDiccionario1)
print(miDiccionario)