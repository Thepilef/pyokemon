cadena = "Python es genial"

vocales = 0

for letra in cadena.lower():
    if letra in "aeiou":
        vocales += 1

print(vocales)
