tupla_vacia = ()
print(tupla_vacia)

# Como las tuplas son inmutables, no podemos agregar elementos directamente.
# Sin embargo, podemos redefinir la tupla para agregarle elementos de la siguiente manera:

tupla_vacia = tupla_vacia + ("valor1", "valor2", "valor3")
print(tupla_vacia)