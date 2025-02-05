#Es posible usar una estructura condicional dentro de otra, aunque se 
#recomienda usarlas con moderacion para evitar que el codigo se vuelva
#dificil de leer

edad = 20
tieneIdentificacion = True

if edad >= 18:
    if tieneIdentificacion:
        print("puedes ingresar")
    else:
        print("necesitas una identificacion")
else:
    print("eres menor de edad")