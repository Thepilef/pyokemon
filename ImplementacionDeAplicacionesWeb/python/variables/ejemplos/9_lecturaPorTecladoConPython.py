#el comando input() en Python se utiliza para tomar entradas del usuario durante la ejecucion
#de un programa. Permite pausar el programa y esperar a que el usuario ingrese texto, que 
#luego se puede procesar o almacenar en una variable

input("aqui va el prompt")

#prompt (opcional): una cadena de texto que se muestra al usuario como mensaje. es util
#para indicar que tipo de entrada se espera. si no se proporciona, no se muestra ningun mensaje

valor = input()

#con esto puedo hacer el tipico mensaje de introuduce un valor
numero = input("introduce un numero: ")
print(numero)

#si quiero hacer algo con el resultado obtenido de lo anterios, debo pasarle la opcion int
#a la variable de antes:
numero = int(numero)

#debo poner la variable = int(variable) y ahora ya se puede sumar o hacer lo que quiera:
print(numero + 10)

#si el usuario pone un numero decimal, tenemos que poner float, en lugar de int:
numero = input("introduce un numero con decimales: ")

#aqui abajo indico que el usuario va a introducir un numero con decimales
numero = float(numero)
print(numero)

#y ya puede operar con el numero
print(numero + 5)

#con float tambien puede introducir tanto enteros como decimales
#tambien puedo hacer todo lo anterior en una misma linea a la vez con numero entero:
numero = float(input("introduce un numero decimal o entero: "))
print(numero + 5)

#y ahora lo mismo pero con numero decimal:
numero = int(input("introduce un numero entero: "))
print(numero + 10)

#tambien puedo hacer esto con nombres, y el input se guarde en en nombre
nombre = input("Introduce tu nombre: ")
print(nombre)
