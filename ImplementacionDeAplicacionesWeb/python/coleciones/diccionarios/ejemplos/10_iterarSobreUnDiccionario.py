miDiccionario = {
    "nombre": "Andres",
    "edad": 21,
    "ciudad": "Madrid"
}

#iterar sobre claves:
for clave in miDiccionario:
    print(clave)

#iterar sobre valores:
for valor in miDiccionario.values():
    print(valor)

#iterar sobre pares valor, clave
for clave, valor in miDiccionario.items():
    print(clave, valor)
