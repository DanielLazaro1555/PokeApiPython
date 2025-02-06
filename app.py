import requests
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from io import BytesIO

# Obtener la lista de Pokémon desde la API


def obtener_lista_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return [pokemon["name"] for pokemon in datos["results"]]
    return []

# Función para obtener información del Pokémon seleccionado


def obtener_pokemon():
    pokemon = entrada.get().strip().lower()
    if not pokemon:
        messagebox.showwarning(
            "Entrada Vacía", "Por favor, ingrese el nombre de un Pokémon.")
        return

    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    respuesta = requests.get(URL)

    if respuesta.status_code == 200:
        datos = respuesta.json()

        # Obtener movimientos y tipos
        movimientos = [move["move"]["name"] for move in datos["moves"][:5]]
        tipos = [tipo["type"]["name"] for tipo in datos["types"]]

        # Obtener la URL de la imagen del Pokémon
        sprite_url = datos["sprites"]["front_default"]

        # Descargar la imagen
        imagen_respuesta = requests.get(sprite_url)
        imagen_pokemon = Image.open(BytesIO(imagen_respuesta.content))
        imagen_pokemon = imagen_pokemon.resize((150, 150))  # Ajustar tamaño
        img = ImageTk.PhotoImage(imagen_pokemon)

        # Mostrar imagen
        label_imagen.config(image=img)
        label_imagen.image = img

        # Mostrar información formateada
        info_texto.set(
            f"🟢 Pokémon: {pokemon.capitalize()}\n\n🔥 Tipos: {', '.join(tipos)}\n\n⚡ Movimientos: {', '.join(movimientos)}")
    else:
        messagebox.showerror(
            "Error", "❌ Pokémon no encontrado. Verifica el nombre e intenta de nuevo.")

# Función para actualizar la lista de sugerencias


def actualizar_sugerencias(event):
    entrada["values"] = [
        p for p in lista_pokemon if p.startswith(entrada.get().lower())]


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("🔍 PokéAPI - Busca tu Pokémon")
ventana.geometry("500x500")
ventana.resizable(False, False)
ventana.configure(bg="#f0f0f0")

# Obtener la lista de Pokémon
lista_pokemon = obtener_lista_pokemon()

# Estilos de fuente
fuente_titulo = ("Arial", 14, "bold")
fuente_texto = ("Arial", 12)

# Etiqueta de instrucciones
tk.Label(ventana, text="Ingrese el nombre del Pokémon:",
         font=fuente_titulo, bg="#f0f0f0").pack(pady=10)

# Campo de entrada con autocompletado
entrada = ttk.Combobox(ventana, font=fuente_texto,
                       values=lista_pokemon, width=25)
entrada.pack(pady=5)
entrada.bind("<KeyRelease>", actualizar_sugerencias)

# Botón de búsqueda
boton_buscar = tk.Button(ventana, text="🔍 Buscar", font=fuente_titulo, bg="#4CAF50",
                         fg="white", padx=10, pady=5, relief="raised", borderwidth=3, command=obtener_pokemon)
boton_buscar.pack(pady=10)

# Área de imagen del Pokémon
label_imagen = tk.Label(ventana, bg="#f0f0f0")
label_imagen.pack(pady=10)

# Área de resultados con caja de texto
info_texto = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=info_texto, font=fuente_texto, bg="white",
                           fg="black", justify="left", wraplength=450, relief="solid", borderwidth=2, padx=10, pady=5)
label_resultado.pack(pady=10, fill="both", expand=True)

# Ejecutar la ventana
ventana.mainloop()
