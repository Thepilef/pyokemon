import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Función para obtener los datos del Pokémon
def obtener_datos(pokemon_nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_nombre}"

    response = requests.get(url)
    if response.ok:
        data = response.json()
        nombre = data["name"].capitalize()
        altura = data["height"] / 10  # Convertir de decímetros a metros
        peso = data["weight"] / 10  # Convertir de hectogramos a kilogramos
        tipos = [tipo["type"]["name"].capitalize() for tipo in data["types"]]

        # Obtener la imagen
        imagen_url = data["sprites"]["front_default"]
        img_response = requests.get(imagen_url)
        img_data = Image.open(BytesIO(img_response.content))
        img_data = img_data.resize((150, 150))  # Redimensionar imagen
        img_tk = ImageTk.PhotoImage(img_data)

        return nombre, altura, peso, tipos, img_tk
    else:
        return None

# Función para comparar los dos Pokémon por altura
def comparar_pokemones():
    pokemon1 = entrada1.get().lower()
    pokemon2 = entrada2.get().lower()

    datos1 = obtener_datos(pokemon1)
    datos2 = obtener_datos(pokemon2)

    if datos1 and datos2:
        nombre1, altura1, peso1, tipos1, img1 = datos1
        nombre2, altura2, peso2, tipos2, img2 = datos2

        # Mostrar los datos en las etiquetas (en columnas)
        label_resultados1.config(text=f"Nombre: {nombre1}\nAltura: {altura1} m\nPeso: {peso1} kg\nTipo(s): {', '.join(tipos1)}")
        label_resultados2.config(text=f"Nombre: {nombre2}\nAltura: {altura2} m\nPeso: {peso2} kg\nTipo(s): {', '.join(tipos2)}")

        # Mostrar las imágenes
        label_imagen1.config(image=img1)
        label_imagen1.image = img1
        label_imagen2.config(image=img2)
        label_imagen2.image = img2

        # Comparar la altura de ambos Pokémon
        if altura1 > altura2:
            resultado = f"{nombre1} es más alto que {nombre2}."
        elif altura2 > altura1:
            resultado = f"{nombre2} es más alto que {nombre1}."
        else:
            resultado = f"{nombre1} y {nombre2} tienen la misma altura."

        label_comparacion.config(text=resultado)
    else:
        messagebox.showerror("Error", "Uno o ambos Pokémon no se encontraron. Intenta nuevamente.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Comparar Pokémon")

# Instrucciones
label_instrucciones = tk.Label(ventana, text="Ingresa el nombre de dos Pokémon para comparar:")
label_instrucciones.pack(pady=10)

# Campos de búsqueda para dos Pokémon
entrada1 = tk.Entry(ventana, width=30)
entrada1.pack(pady=5)

entrada2 = tk.Entry(ventana, width=30)
entrada2.pack(pady=5)

# Botón para comparar
boton_comparar = tk.Button(ventana, text="Comparar", command=comparar_pokemones)
boton_comparar.pack(pady=10)

# Crear un marco para las columnas de datos
frame_columnas = tk.Frame(ventana)
frame_columnas.pack(pady=20)

# Crear columnas dentro del marco
frame_pokemon1 = tk.Frame(frame_columnas)
frame_pokemon1.pack(side="left", padx=20)

frame_pokemon2 = tk.Frame(frame_columnas)
frame_pokemon2.pack(side="left", padx=20)

# Etiquetas para mostrar los resultados de los Pokémon
label_resultados1 = tk.Label(frame_pokemon1, text="", justify="left")
label_resultados1.pack()

label_imagen1 = tk.Label(frame_pokemon1)
label_imagen1.pack(pady=10)

label_resultados2 = tk.Label(frame_pokemon2, text="", justify="left")
label_resultados2.pack()

label_imagen2 = tk.Label(frame_pokemon2)
label_imagen2.pack(pady=10)

# Etiqueta para mostrar el resultado de la comparación
label_comparacion = tk.Label(ventana, text="", justify="left")
label_comparacion.pack(pady=10)

# Iniciar la ventana
ventana.mainloop()
