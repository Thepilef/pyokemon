numero = int(input("escribe un numero: "))
factorial = 1

while numero > 1:
    factorial *= numero
    numero -= 1

print(factorial)