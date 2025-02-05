#pide al usuario al precio de un producto. si el precio es mayor a 1000
#aplica un descuento del 10% y muestra el precio final. si no, muestra
#el precio sin descuento

precio = int(input("escriba el precio de su producto: "))

if precio >= 1000:
    precio = precio - precio / 10

print(precio)