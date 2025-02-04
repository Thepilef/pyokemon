#define una funcion llamada es_par que acepte un numero y devuelva true si el numero es par
#y inpar si el numero es inpar
#prueba con diferentes valores

def es_par(x):
    if x % 2 != 0:
        return "true"
    else:
        return "false"

ejemplo1 = es_par(1)
print(ejemplo1)
ejemplo2 = es_par(2)
print(ejemplo2)
ejemplo3 = es_par(3)
print(ejemplo3)
ejemplo4 = es_par(4)
print(ejemplo4)
ejemplo5 = es_par(5)
print(ejemplo5)


def es_par1(numero):
    return numero % 2 == 0

print(es_par1(6))
print(es_par1(7))
print(es_par1(8))
print(es_par1(9))