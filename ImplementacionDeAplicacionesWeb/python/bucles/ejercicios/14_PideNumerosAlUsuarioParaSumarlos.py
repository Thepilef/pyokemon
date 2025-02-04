numero = 1
suma = 0
lista = []

while numero != 0:
    numero = int(input("Escribe un numero: "))
    if numero != 0:
        print(f"{suma} + {numero} = {suma + numero}")
        suma += numero
        lista.append(numero)
        print(lista)
        






