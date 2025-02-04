productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}

suma = 0

for clave, valor in productos.items():
    suma += valor
    print(suma)