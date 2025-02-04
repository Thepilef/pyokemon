#define una funcion llamada saludar_con_titulo que acepte dos parametros: nombre y titulo,
#con un valor por defecto para titulo
#prueba la funcion con y sin el parametro

def saludar_con_titulo(nombre, titulo="señor"):
    print(f"buenos dias {titulo} {nombre}")

saludar_con_titulo("Andres", "mr")
saludar_con_titulo("Andres")
