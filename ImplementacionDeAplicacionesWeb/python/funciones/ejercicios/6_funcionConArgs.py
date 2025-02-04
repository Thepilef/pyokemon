#define una funcion llamada promedio que acepte una cantidad arbitraria de numeros y devuelva su promedio
#prueba la cantidad con diferentes cantidades de argumentos

def promedio(*args):
    suma = 0
    cantidad = 0
    for numero in args:
        suma += numero
        cantidad += 1
    return suma / cantidad

print(promedio(4,45,24,6))
print(promedio(2,5,4,2))
print(promedio(5,5,5,5,5))


def promedio1(*args):
    return sum(args) / len(args) if args else None