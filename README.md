# 🔍 PokéAPI GUI - Busca tu Pokémon

## 📌 Descripción

Esta es una aplicación de **interfaz gráfica (GUI)** en **Python** que permite buscar Pokémon y obtener información como su **imagen, tipo y movimientos principales**.

La interfaz incluye:

- ✅ **Autocompletado** mientras escribes el nombre del Pokémon.
- ✅ **Imagen del Pokémon** obtenida en tiempo real.
- ✅ **Movimientos y tipos del Pokémon** de la **PokéAPI**.
- ✅ **Diseño atractivo y fácil de usar** con `Tkinter`.

---

## 🚀 Tecnologías utilizadas

| Tecnología   | Descripción                                             |
| ------------ | ------------------------------------------------------- |
| **Python**   | Lenguaje de programación utilizado.                     |
| **FastAPI**  | API de PokéAPI para obtener información de los Pokémon. |
| **Tkinter**  | Librería estándar de Python para interfaces gráficas.   |
| **Pillow**   | Manejo de imágenes dentro de la GUI.                    |
| **Requests** | Peticiones HTTP para obtener datos desde la API.        |

---

## 📂 Instalación y ejecución

### 🔹 **1️⃣ Clonar el repositorio**

```bash
git clone https://github.com/tuusuario/PokeAPI-GUI.git
cd PokeAPI-GUI
```

🔹 2️⃣ Crear un entorno virtual (Opcional)

python3 -m venv venv
source venv/bin/activate # En Linux/macOS
venv\Scripts\activate # En Windows

🔹 3️⃣ Instalar dependencias

pip install -r requirements.txt

Si no tienes el archivo requirements.txt, instala manualmente las dependencias:

pip install requests pillow tk

🔹 4️⃣ Ejecutar la aplicación

python3 app.py

## 🎨 Captura de pantalla

![PokéAPI GUI](Captura%20desde%202025-02-06%2018-27-21.png)
