#¿Qué es una función?
#Una función es un bloque de código que realiza una tarea específica. 
#Las funciones ayudan a organizar el código, hacerlo más legible y reutilizable.

#Definición de una función
#Para definir una función en Python, se utiliza la palabra clave def seguida 
#del nombre de la función y paréntesis. Aquí tienes un ejemplo básico:

def saludar():
    print("¡Hola, mundo!")

#Llamada a una función
#Para llamar a una función, simplemente escribe 
#su nombre seguido de paréntesis:
saludar()

#prametros y argumentos
#las funciones pueden aceptar parametros, que son variables que se pasan
#a la funcion. Aqui tienes un ejemplo:
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

#llamada a la funcion con un argumento
saludar("Andres")

#valores de retorno
#las funciones pueden devolver valores utilizando la palabra clave return:
def sumar(a, b):
    return a + b

#llamada a la funcion y almacenamiento del valor de entorno
resultado = sumar(3, 5)
print(resultado)

#parametros por defecto
#puedes definir valores por defecto para los parametros. si no se proporciona
#un argumento, se utilizara el valor por defecto:
def saludar(nombre="Mundo"):
    print(f"¡Hola, {nombre}!")

#llamada a la funcion sin argumento:
saludar()

#parametros arbitrarios
#si no sabes cuantos argumentos se pasaran a tu funcion, puedes usar
# *args para recibir una cantidad arbitraria de argumentos

def sumarTodos(*args):
    return sum(args)

#llamada a la funcion con multiples parametros
resultado = sumarTodos(1, 2, 3, 4)
print(resultado)

#parametros con nombres arbitrarios
#si quieres aceptar un numero arbitrario de parametros con nombre, usa kwargs
def imprimirInfo(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

#llamada a la funcion con parametros con nombre:
imprimirInfo(nombre="Andres", edad=21, ciudad="Bogota")

#funciones anidadas 
#puedes definir funciones dentro de otras funciones:
def exterior():
    print("esta es la funcion exterior")

    def interior():
        print("esta es la funcion interior")
    
    interior()

#llamada a la funcion exterior
exterior()

#funciones como objetos de primera clase
#en python, las funciones son objetos de primera clase, lo que significa que
#puedes pasarlas como argumentos a otras funciones, devolverlas desde otras
#funciones y asignarlas a variables
def multiplicarPorDos(x):
    return x * 2

def aplicarFuncion(func, valor):
    return func(valor)

resultado = aplicarFuncion(multiplicarPorDos, 10)
print(resultado)

#la funcion main
#en python, no hay una funcion main obligatoria como en otros lenguajes,
#pero es una buena practica definir una funcion principal y usar la siguiente
#estructura para ejecutar el codigo principal:
def main():
    print("este es el punto de entrada principal del programa")

if __name__ == "__main__":
    main()
    
