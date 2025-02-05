#permite evaluar multiples condiciones de forma secuencial. si una condicion
#es verdadera, se ejecuta su bloque asociado y se ignoran las demas
# if condidion1:
#   codigo si condicion1 es verdadera
# elif condicion2:
#   codigo si condicion2 es verdadera
# else:
#   codigo si ninguna de las condiciones es verdadera

temperatura = 3
if temperatura > 30:
    print("Hace mucho calor")
elif temperatura > 20:
    print("El clima es agradable")
else:
    print("Hace frio")