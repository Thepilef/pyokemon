#define una funcion llamada imprimir_detalles que acepte una cantidad arbitraria de parametros
#con nombre y los imprima en formato clave-valor
#prueba la funcion con diferentes conjuntos de parametros

def imprimir_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"clave {clave}: valor {valor}")

imprimir_detalles(nombre="andres", edad=21, ciudad="Bogota")