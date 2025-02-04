productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}

mayores1 = []

for clave, valor in productos.items():
    if valor > 1:
        mayores1.append(clave)

print(mayores1)